from app.db.database import user_collection
from app.core.security import hash_password, verify_password, access_token_generator
from fastapi import HTTPException

from app.schemas.user_schema import UserCreate
from app.utils.status_codes import BAD_REQUEST


async def signup_service(user: UserCreate):
    existing_user = await user_collection().find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=BAD_REQUEST, detail="User already exists")

    hashed_password = hash_password(user.password)
    user.password = hashed_password

    await user_collection().insert_one(user.model_dump())
    token = access_token_generator({"sub": user.email})
    return {"access_token": token, "token_type": "Bearer"}


async def login_service(user):
    db_user = await user_collection().find_one({"email": user.email})
    if not db_user:
        raise HTTPException(status_code=BAD_REQUEST, detail="Invalid credentials")

    if not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=BAD_REQUEST, detail="Invalid credentials")

    token = access_token_generator({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}