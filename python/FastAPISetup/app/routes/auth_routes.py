from fastapi import APIRouter, Depends

from app.core.dependencies import get_current_user
from app.schemas.user_schema import UserCreate, UserLogin
from app.controllers.auth_controller import signup_controller, login_controller

router = APIRouter(prefix="/auth", tags=["auth", "Auth Routes"])


# for route level security
#router = APIRouter(prefix="/auth", tags=["auth", "Auth Routes"], dependencies=[Depends(get_current_user)])

@router.post("/signup")
async def signup(user: UserCreate):
    return await signup_controller(user)

@router.post("/login")
async def login(user: UserLogin):
    return await login_controller(user)

@router.get("/profile")
async def get_profile(current_user: dict = Depends(get_current_user)):
    return {
        "email": current_user["email"],
        "message": "You are authorized 🔐"
    }