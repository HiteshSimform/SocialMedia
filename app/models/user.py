from sqlalchemy import Column, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base
from models.base import BaseMixin


class User(Base, BaseMixin):
    """Application user."""
    __tablename__ = "users"

    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    role = Column(String(50), default="user")

    profile = relationship("Profile", back_populates="user", uselist=False)
    posts = relationship("Post", back_populates="user")


class Profile(Base, BaseMixin):
    """User profile data."""
    __tablename__ = "profiles"

    user_id = Column(ForeignKey("users.id"), nullable=False, unique=True)
    bio = Column(String(255))
    avatar_url = Column(String(255))
    website = Column(String(255))
    gender = Column(String(10))
    dob = Column(Date)

    user = relationship("User", back_populates="profile")
