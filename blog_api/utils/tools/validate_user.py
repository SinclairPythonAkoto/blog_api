from typing import Dict
from blog_api import app
from blog_api.extension import SessionLocal, db_session
from blog_api.models.users import Users
from flask_restful import abort


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
        abort(409, message="The username already exists, please choose a different username.")
    
def abort_if_email_already_exists_409(session: db_session, email: str):
    """Raises HTTPExecption if username already found in Users db."""
    result: bool = session.query(
        session.query(Users).filter_by(email=email).exists()
    ).scalar()
    if result is True:
        abort(409, message="This email is already linked to another account, please choose a different email.")