import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return "server 3"


if __name__ == "__main__":
    uvicorn.run("server3:app", port=8000, reload=True)
