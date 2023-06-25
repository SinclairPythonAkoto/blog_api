from typing import Dict
from blog_api import app
from blog_api.extension import SessionLocal
from blog_api.models.users import Users


def get_username(username: str) -> Users[Dict]:
    """Finds user by username."""
    with app.app_context():
        session: SessionLocal = SessionLocal()
        find_user: Users = session.query(Users).filter_by(username=username).first()
    return find_user

def get_email(email: str) -> Users[Dict]:
    """Finds user by email."""
    with app.app_context():
        session: SessionLocal = SessionLocal()
        find_email: Users = session.query(Users).filter_by(email=email).first()
    return find_email

def validate_username(username: str) -> bool:
    """Checks Users db to see if username exists."""
    with app.app_context():
        session: SessionLocal = SessionLocal()
        result: bool = session.query(
            session.query(Users).filter_by(username=username).exists()
        ).scalar()
    return result

def validate_email(email: str) -> bool:
    """Checks Users db to see if email exists."""
    with app.app_context():
        session: SessionLocal = SessionLocal()
    result: bool = session.query(
            session.query(Users).filter_by(email=email).exists()
        ).scalar()
    return result

def validate_password(password: str) -> bool:
    """Checks Users db to see if password exists."""
    with app.app_context():
        session: SessionLocal = SessionLocal()
    result: bool = session.query(
            session.query(Users).filter_by(password=password).exists()
        ).scalar()
    return result