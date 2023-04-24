import logging

from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from .auth import registration_user, authentication_user
from .schemas import User, AuthUser, ResponseForAuth, ResponseForReg


logger = logging.getLogger(name=__name__)


templates = Jinja2Templates(directory="src/auth/templates")


auth_router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@auth_router.post("/registration", response_model=ResponseForReg)
async def registration(user: User):
    logger.info(f"name: {user.name}; email: {user.email};"
                f" password: {user.password}")
    registration_status = registration_user(name=user.name,
                                            email=user.email,
                                            password=user.password)
    user_json = {"name": user.name, "email": user.email}

    if not registration_status:
        return {"status": "not success", "addable_user": "It user already registration"}

    return {"status": "success", "addable_user": user_json}


@auth_router.get("/authentication", response_class=HTMLResponse)
async def authentication(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@auth_router.post("/authentication/postdata", response_model=ResponseForAuth)
async def authentication_post():
    if not authentication_user(email=user.email, password=user.password):
        return {
            "status": "not success",
            "state": "Not true email or password!"
        }

    return {
        "status": "success",
        "state": "You have successfully passed verification!"
    }