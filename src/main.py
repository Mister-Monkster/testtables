from fastapi import FastAPI
import uvicorn

from routers.reservation_router import reservation_router
from routers.table_router import table_router

app = FastAPI()

app.include_router(table_router)
app.include_router(reservation_router)


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="localhost",
        port=8000,

    )