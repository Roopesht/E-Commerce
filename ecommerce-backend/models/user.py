from passlib.context import CryptContext

# Use a scheme that doesn't depend on the external `bcrypt` package.
# This avoids runtime failures caused by passlib/bcrypt version incompatibilities.
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def hash_password(password:str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password:str, hashed_password:str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_user_document(
        firstname: str,
        lastname:str,
        mobilenumber:str,
        username:str,
        password:str
) -> dict:
    return {
        "firstname": firstname,
        "lastname": lastname,
        "mobilenumber": mobilenumber,
        "username": username,
        "password": hash_password(password)
    }