from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship
class blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String, index=True)
    creator_id = Column(Integer, ForeignKey("users.id"))

    creator = relationship("users", back_populates="blogs")
class users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)  
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship("blog", back_populates="creator")