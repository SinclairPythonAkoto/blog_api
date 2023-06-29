import functools
from typing import Dict
from blog_api import app
from blog_api.extension import SessionLocal, db_session
from blog_api.models.users import Users
from flask_restful import abort
from hmac import compare_digest
from blog_api.utils.tools.user_token import generate_user_token
from flask import request


def get_username(session: db_session, username: str) -> Users:
    """Finds user by username."""
    find_user: Users = session.query(Users).filter_by(username=username).first()
    return find_user


def get_email(session: db_session, email: str) -> Users:
    """Finds user by email."""
    find_email: Users = session.query(Users).filter_by(email=email).first()
    return find_email


def validate_username(session: db_session, username: str) -> bool:
    """Checks Users db to see if username exists."""
    result: bool = session.query(
        session.query(Users).filter_by(username=username).exists()
    ).scalar()
    return result


def validate_email(session: db_session, email: str) -> bool:
    """Checks Users db to see if email exists."""
    result: bool = session.query(
        session.query(Users).filter_by(email=email).exists()
    ).scalar()
    return result


def validate_password(session: db_session, password: str) -> bool:
    """Checks Users db to see if password exists."""
    result: bool = session.query(
        session.query(Users).filter_by(password=password).exists()
    ).scalar()
    return result


def abort_if_username_already_exists_409(session: db_session, username: str):
    """Raises HTTPExecption if username already found in Users db."""
    result: bool = session.query(
        session.query(Users).filter_by(username=username).exists()
    ).scalar()
    if result is True:
        abort(
            409,
            message="The username already exists, please choose a different username.",
        )


def abort_if_email_already_exists_409(session: db_session, email: str):
    """Raises HTTPExecption if username already found in Users db."""
    result: bool = session.query(
        session.query(Users).filter_by(email=email).exists()
    ).scalar()
    if result is True:
        abort(
            409,
            message="This email is already linked to another account, please choose a different email.",
        )

def authenticate_user_key(session: db_session, user_key: str) -> bool:
    """Checks if the user key exists in the db.
    """
    check_key: str = session.query(Users).filter_by(user_key=user_key).first()
    if check_key and compare_digest(check_key, user_key):
        # check_key.user_key = generate_user_token()
        # session.commit()
        return True
    

def user_key_required(func):
    """Checks for a valid user key to gain access to private API routes."""
    @functools.wraps(func)
    def check_user_key(*args, **kwargs):
        if request.json:
            user_key: request = request.json.get("user_key")
        else:
            abort(400, message="Please provide a user API key.")
        # check if API key is correct & valid
        if request.method == "POST" and authenticate_user_key(user_key):
            return func(*args, **kwargs)
        else:
            abort(403, message="The user API key is not valid.")
    return check_user_key