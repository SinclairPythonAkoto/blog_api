from blog_api.extension import db_session
from blog_api.models.users import Users
from flask_restful import abort


def abort_if_username_not_found_404(session: db_session, user: str):
    """Raises HTTPExecption if no username found in Users db."""
    result: bool = session.query(
        session.query(Users).filter_by(username=user).exists()
    ).scalar()
    if result == False:
        abort(404, message="Username not found.")


def abort_if_no_email_404(session: db_session, user_email: str):
    """Raises HTTPExecption if no email found in Users db."""
    result: bool = session.query(
        session.query(Users).filter_by(email=user_email).exists()
    ).scalar()
    if result == False:
        abort(404, message="Email not found.")


def abort_if_username_already_exists_409(session: db_session, username: str):
    """Raises HTTPExecption if username already found in Users db."""
    result: bool = session.query(
        session.query(Users).filter_by(username=username).exists()
    ).scalar()
    if result == True:
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
