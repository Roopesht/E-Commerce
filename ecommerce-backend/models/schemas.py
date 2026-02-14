from pydantic import BaseModel

class RegisterRequest(BaseModel):
    firstname: str
    lastname: str
    mobilenumber: str
    username: str
    password: str
    confirm_password: str

class RegisterResponse(BaseModel):
    message: str

class LoginRequest(BaseModel):
    username: str
    password: str

class ProductResponse(BaseModel):
    id: str
    name: str
    description: str
    price: float
    image_url: str
    stock: int

class ADDPRODUCTRequest(BaseModel):
    name: str
    description: str
    price: float
    image_url: str
    stock: int