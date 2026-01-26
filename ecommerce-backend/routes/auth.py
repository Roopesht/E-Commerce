from fastapi import APIRouter, HTTPException, status
from database import db
from models.user import create_user_document
from models.schemas import RegisterRequest, RegisterResponse
from models.schemas import LoginRequest
from models.user import verify_password

router = APIRouter()
users_collection = db["users"]


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=RegisterResponse)
def register_user(user: RegisterRequest) -> RegisterResponse:
    existing_user = users_collection.find_one({"username": user.username})
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    user_doc = create_user_document(
        firstname=user.firstname,
        lastname=user.lastname,
        mobilenumber=user.mobilenumber,
        username=user.username,
        password=user.password
    )

    users_collection.insert_one(user_doc)

    return {"message": "User registered successfully"}

@router.post("/login")
def login_user(credentials: LoginRequest):
    user = users_collection.find_one({"username": credentials.username})
    if not user or not verify_password(credentials.password, user["password"]):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    
    return {
        "message": "Login successful",
        "username": user["username"]
    }