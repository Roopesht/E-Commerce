from fastapi import APIRouter, HTTPException, status
from firestore import get_document, add_document
from models.user import create_user_document
from models.schemas import RegisterRequest, RegisterResponse
from models.schemas import LoginRequest
from models.user import verify_password

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=RegisterResponse)
def register_user(user: RegisterRequest) -> RegisterResponse:
    # Use username as document ID for easy lookups
    existing_user = get_document("users", user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    if user.password != user.confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    user_doc = create_user_document(
        firstname=user.firstname,
        lastname=user.lastname,
        mobilenumber=user.mobilenumber,
        username=user.username,
        password=user.password,
        confirm_password=user.confirm_password
    )

    add_document("users", user_doc, doc_id=user.username)

    return {"message": "User registered successfully"}

@router.post("/login")
def login_user(credentials: LoginRequest):
    user = get_document("users", credentials.username)
    if not user or not verify_password(credentials.password, user["password"]):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    
    return {
        "message": "Login successful",
        "username": user["username"]
    }