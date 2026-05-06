import os
import uuid
from typing import Dict, List, Optional
from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
import json

app = FastAPI(title="Real-Time Polls API")

@app.get("/hello")
def hello():
    return {"message": "works"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- In-memory store ---
polls: Dict[str, dict] = {}

# --- WebSocket manager ---
class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, List[WebSocket]] = {}

    async def connect(self, poll_id: str, websocket: WebSocket):
        await websocket.accept()
        if poll_id not in self.active_connections:
            self.active_connections[poll_id] = []
        self.active_connections[poll_id].append(websocket)

    def disconnect(self, poll_id: str, websocket: WebSocket):
        if poll_id in self.active_connections:
            self.active_connections[poll_id].remove(websocket)

    async def broadcast(self, poll_id: str, message: dict):
        if poll_id in self.active_connections:
            dead = []
            for connection in self.active_connections[poll_id]:
                try:
                    await connection.send_json(message)
                except Exception:
                    dead.append(connection)
            for d in dead:
                self.active_connections[poll_id].remove(d)

manager = ConnectionManager()

# --- Models ---
class PollCreate(BaseModel):
    question: str
    options: List[str]

class VoteRequest(BaseModel):
    option: str

# --- REST Endpoints ---

@app.post("/polls", status_code=201)
def create_poll(body: PollCreate):
    poll_id = str(uuid.uuid4())
    polls[poll_id] = {
        "id": poll_id,
        "question": body.question,
        "options": {opt: 0 for opt in body.options},
    }
    return polls[poll_id]

@app.get("/polls")
def list_polls():
    return list(polls.values())

@app.get("/polls/{poll_id}")
def get_poll(poll_id: str):
    if poll_id not in polls:
        raise HTTPException(status_code=404, detail="Poll not found")
    return polls[poll_id]

@app.post("/polls/{poll_id}/vote")
async def vote_rest(poll_id: str, body: VoteRequest):
    if poll_id not in polls:
        raise HTTPException(status_code=404, detail="Poll not found")
    if body.option not in polls[poll_id]["options"]:
        raise HTTPException(status_code=400, detail="Invalid option")
    polls[poll_id]["options"][body.option] += 1
    # Broadcast update to all WebSocket clients on this poll
    await manager.broadcast(poll_id, {"type": "update", "poll": polls[poll_id]})
    return polls[poll_id]

@app.delete("/polls/{poll_id}", status_code=204)
def delete_poll(poll_id: str):
    if poll_id not in polls:
        raise HTTPException(status_code=404, detail="Poll not found")
    del polls[poll_id]

# --- WebSocket Endpoint ---


@app.websocket("/ws/polls/{poll_id}")
async def websocket_endpoint(websocket: WebSocket, poll_id: str):
    if poll_id not in polls:
        await websocket.close(code=4004)
        return

    await manager.connect(poll_id, websocket)
    # Send current poll state on connect
    await websocket.send_json({"type": "connected", "poll": polls[poll_id]})

    try:
        while True:
            data = await websocket.receive_text()
            msg = json.loads(data)

            if msg.get("type") == "vote":
                option = msg.get("option")
                if option not in polls[poll_id]["options"]:
                    await websocket.send_json({"type": "error", "detail": "Invalid option"})
                    continue
                polls[poll_id]["options"][option] += 1
                # Broadcast to ALL clients on this poll
                await manager.broadcast(poll_id, {"type": "update", "poll": polls[poll_id]})

    except WebSocketDisconnect:
        manager.disconnect(poll_id, websocket)

@app.get("/index", response_class=HTMLResponse)
async def test_page():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "frontend", "index.html")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()