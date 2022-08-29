import os
import jwt # used for encoding and decoding jwt tokens
from fastapi import HTTPException # used to handle error handling
from passlib.context import CryptContext # used for hashing the password 
from datetime import datetime, timedelta # used to handle expiry time for tokens
from core.settings import SECRET


hasher= CryptContext(schemes=['bcrypt'])


def encode_password( password):
    return hasher.hash(password)


def verify_password(password, encoded_password):
    return hasher.verify(password, encoded_password)


def encode_token(email):
    payload = {
        'exp' : datetime.utcnow() + timedelta(days=0, minutes=30),
        'iat' : datetime.utcnow(),
    'scope': 'access_token',
        'sub' : email
    }
    return jwt.encode(
        payload, 
        SECRET,
        algorithm='HS256'
    )


def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET, algorithms=['HS256'])
        if (payload['scope'] == 'access_token'):
            return payload
        raise HTTPException(status_code=401, detail='Scope for the token is invalid')
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Token expired')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail='Invalid token')


def encode_refresh_token( email):
    payload = {
        'exp' : str((datetime.utcnow() + timedelta(days=0, hours=10)).timestamp()),
        'iat' : str(datetime.utcnow().timestamp()),
    'scope': 'refresh_token',
        'sub' : email
    }
    return jwt.encode(
        payload, 
        SECRET,
        algorithm='HS256'
    )

    
def refresh_token(refresh_token):
    try:
        payload = jwt.decode(refresh_token, SECRET, algorithms=['HS256'])
        if (payload['scope'] == 'refresh_token'):
            email = payload['sub']
            new_token = encode_token(email)
            return new_token
        raise HTTPException(status_code=401, detail='Invalid scope for token')
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Refresh token expired')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail='Invalid refresh token')


def check_auth_user(encode_token):
    token=decode_token(encode_token)
    if datetime.utcnow().timestamp()>int(token['exp']):
        raise HTTPException(status_code=401, detail='goodby, time is not valid')
    else:
        return True

    
