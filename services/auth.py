import jwt
from passlib.context import CryptContext

SECRET_KEY = "secret"


def create_access_token(data: dict):
    access_token = jwt.encode(data, SECRET_KEY, algorithm="HS256")
    return access_token


# Khai báo hàm xác thực token
def decode_access_token(token: str):
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded_token
    except:
        return None


# Tạo password hash sử dụng PassLib
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
