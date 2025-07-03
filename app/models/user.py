from enum import Enum
from sqlalchemy import Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, Date, ForeignKey
from typing import Optional, List
from db.base import Base
from models.base import BaseMixin
import uuid


# Enum for Gender
class GenderEnum(Enum):
    MALE = "male"
    FEMALE = "female"
    NON_BINARY = "non_binary"
    OTHER = "other"
    PREFER_NOT_TO_SAY = "prefer_not_to_say"


# User Model
class User(Base, BaseMixin):
    """
    Represents an application user.

    Attributes:
        username (str): Unique username.
        email (str): User email address.
        password_hash (str): Hashed password.
        is_active (bool): Whether the account is active.
        is_verified (bool): Whether email is verified.
        role (str): User role (e.g., 'user', 'admin').
    """

    __tablename__ = "users"
    username: Mapped[str] = mapped_column(
        String(50), unique=True, index=True, nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(100), unique=True, index=True, nullable=False
    )
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    role: Mapped[str] = mapped_column(String(50), default="user")

    profile: Mapped[Optional["Profile"]] = relationship(
        back_populates="user", uselist=False
    )
    posts: Mapped[List["Post"]] = relationship(back_populates="user")


# Profile Model with Gender Enum
class Profile(Base, BaseMixin):
    """
    Represents additional user profile data.

    Attributes:
        bio (str): User biography text.
        avatar_url (str): Profile image URL.
        website (str): Personal website.
        gender (str): Gender identity.
        dob (Date): Date of birth.
    """

    __tablename__ = "profiles"
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"), unique=True, nullable=False
    )
    bio: Mapped[Optional[str]] = mapped_column(String(255))
    avatar_url: Mapped[Optional[str]] = mapped_column(String(255))
    website: Mapped[Optional[str]] = mapped_column(String(255))

    # Gender as Enum
    gender: Mapped[Optional[GenderEnum]] = mapped_column(
        SAEnum(
            GenderEnum,
            values_callable=lambda obj: [e.value for e in obj],
            nullable=True,
        )
    )

    dob: Mapped[Optional[Date]] = mapped_column(Date)

    user: Mapped["User"] = relationship(back_populates="profile")
