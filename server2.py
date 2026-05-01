import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "server 2"


if __name__ == "__main__":
    uvicorn.run("server2:app", port=5000, reload=True)
