import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "Server 1"


if __name__ == "__main__":
    uvicorn.run("server1:app", port=3000, log_level="info", reload=True)
