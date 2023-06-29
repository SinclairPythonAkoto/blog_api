from sqlalchemy import Column, String, Integer, DateTime, Text, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from blog_api.extension import Base


class Users(Base):
    __tablename__ = "users"
    id = Column("id", Integer, primary_key=True)
    username = Column("username", String(35), nullable=False)
    password = Column("password", String(50), nullable=False)
    email = Column("email", String(50), nullable=False)
    created = Column("created", DateTime, nullable=False)
    user_key = Column("session_key", String(50), nullable=False)
    blog = relationship("Blog", backref="blog")   # set relationship with blog db

    def __init__(self, username, password, email, created, blog, user_key=None):
        self.username = username
        self.password = password
        self.email = email
        self.created = created
        self.user_key = user_key
        self.blog = blog
        
# class Blog(Base):
#     __table__name = "blog"
#     id = Column("id", Integer, primary_key=True)
#     title = Column("title", String(65), nullable=False)
#     content = Column("content", Text, nullable=False)
#     timestamp = Column("timestamp", DateTime, nullable=False)
#     users_id = Column(Integer, ForeignKey("users.id"))    # creates relationship with users db
#     pics = relationship("Images", backref="pics")         # set relationship with images db


# class Images(Base):
#     __tablename__ = "images"
#     id = Column("id", Integer, primary_key=True)
#     title = Column("title", String(50), nullable=True)
#     description = Column("description", String(100), nullable=True)
#     pic = Column("pic", LargeBinary, nullable=False)
#     timestamp = Column("timestamp", DateTime, nullable=False)
#     blog_id = Column(Integer, ForeignKey("blog.id"))    # creates relationship with blog db
