import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()

# this creates an instance of the db
engine: create_engine = create_engine(os.environ["BLOG_DB"])
db_session = scoped_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
# create local session - to query db
SessionLocal: sessionmaker = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

# create a Base for db models
Base: declarative_base = declarative_base()
Base.query = db_session.query_property()

# initialise db
def init_db():
    """Create db models"""
    import blog_api.models

    Base.metadata.create_all(bind=engine)

