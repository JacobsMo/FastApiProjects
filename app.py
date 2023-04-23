import logging

from fastapi import FastAPI
import uvicorn

from src.auth.routers import auth_router


host = "127.0.0.1"
port = 8004


logging.basicConfig(filename='loggs.log', level=logging.DEBUG, \
                        format="%(name)s - %(levelname)s:%(message)s")


if __name__ == '__main__':
    app = FastAPI()
    app.include_router(auth_router)
    uvicorn.run(app, host=host, port=port)


@app.get("/")
def get_menu():
    return {"status": "success"}