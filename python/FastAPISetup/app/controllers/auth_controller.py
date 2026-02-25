from app.schemas.user_schema import TokenResponse
from app.services.auth_service import signup_service as user_signup, login_service as user_login

async def signup_controller(user) -> TokenResponse:
    return await user_signup(user)

async def login_controller(user) -> TokenResponse:
    return await user_login(user)