from typing import Dict
from blog_api import app
from blog_api.extension import SessionLocal, db_session
from blog_api.models.users import Users

def create_account(session: db_session, username: str, email: str, password: str):
    new_account: Users = Users(
        username=username,
        email=email,
        password=password,
    )
    session.add(new_account)
    session.commit()
    return new_account