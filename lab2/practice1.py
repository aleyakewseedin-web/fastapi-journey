from fastapi import FastAPI, Request

app = FastAPI()

# Mock database of crew members
crew = [
    {"id": 1, "name": "Cosmo", "role": "Captain"},
    {"id": 2, "name": "Alice", "role": "Engineer"},
    {"id": 3, "name": "Bob", "role": "Scientist"}
]


@app.post("/add_crew/")
async def add_crew_member(request: Request):
    data = await request.json()
    name = data.get("name")
    role = data.get("role")
    
    if not name or not role:
        return {"error": "Name and role are required"}
    
    new_id = max([member["id"] for member in crew], default=0) + 1
    new_member = {"id": new_id, "name": name, "role": role}
    crew.append(new_member)
    
    return new_member