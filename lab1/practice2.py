from fastapi import FastAPI
import uvicorn

aleya = FastAPI()

if __name__ == "__main__":
    uvicorn.run(aleya, host="127.0.0.1", port=8080)