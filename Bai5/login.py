from auth import (
    verify_password,
    create_access_token
)

def login(data, db):

    # 1. Tìm user bằng email
    user = (
        db.query(User)
        .filter(User.email == data.email)
        .first()
    )
    if user is None:
        return {
            "success": False,
            "message": "Email hoặc mật khẩu không chính xác"
        }
    if not verify_password(
        data.password,
        user.password
    ):
        return {
            "success": False,
            "message": "Email hoặc mật khẩu không chính xác"
        }
    token = create_access_token(
        user_id=user.id,
        email=user.email,
        role=user.role
    )
    return {
        "success": True,
        "message": "Đăng nhập thành công",
        "access_token": token
    }