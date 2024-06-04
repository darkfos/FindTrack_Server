#System
import uvicorn

#Other libraries
from fastapi import FastAPI

app: FastAPI = FastAPI(
    title="FindTracker - Server",
    description="API для компании грузоперевозок."
)


if __name__ == "__main__":
    uvicorn.run(
        "app:main",
        host="127.0.0.1",
        port=6789,
        reload=True
    )