from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext


SECRET_KEY = "my_secret_key"
ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str):
    """
    Mã hóa mật khẩu trước khi lưu database
    """
    return pwd_context.hash(password)


def verify_password(
    password: str,
    hashed_password: str
):
    """
    Kiểm tra password người dùng nhập
    với password đã hash
    """
    return pwd_context.verify(
        password,
        hashed_password
    )


def create_access_token(
    user_id: int,
    email: str,
    role: str
):
    """
    Tạo Access Token
    """

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "email": email,
        "role": role,
        "exp": expire
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token