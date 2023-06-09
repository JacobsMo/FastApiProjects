import logging

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import uvicorn

from src.auth.routers import auth_router


dirs_for_templates = Jinja2Templates(directory="static")


host = "127.0.0.1"
port = 8004


logging.basicConfig(filename='loggs.log', level=logging.DEBUG, \
                        format="%(name)s - %(levelname)s:%(message)s")


app = FastAPI()
app.mount("/static",
          StaticFiles(directory="static"),
          name="static")
app.include_router(auth_router)


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return dirs_for_templates.TemplateResponse("index.html",
                                               {"request": request})


if __name__ == '__main__':
    uvicorn.run(app, host=host, port=port)