import jwt
from settings import secret_key

JWT_SECRET = secret_key
JWT_ALGORITHM = 'HS256'


def encrypt_token(token_info: dict, secret_key:str =JWT_SECRET):
    token = jwt.encode(token_info, secret_key, algorithm=JWT_ALGORITHM)
    return token


def decrypt_token(token: str, secret_key: str=JWT_SECRET) -> dict:
    try:
        token_info = jwt.decode(token, secret_key, algorithms=[JWT_ALGORITHM])
        return token_info
    except Exception as e:
        print('token解密失败!', e)
        return {}