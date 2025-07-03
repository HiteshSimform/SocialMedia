from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base import Base
from models.base import BaseMixin
from models.user import User


class Follow(Base, BaseMixin):
    """Follow relationship."""

    __tablename__ = "follows"

    follower_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    following_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    status: Mapped[str] = mapped_column(String(10), default="accepted")  # or 'pending'

    # Relationships
    follower: Mapped["User"] = relationship("User", foreign_keys=[follower_id])
    following: Mapped["User"] = relationship("User", foreign_keys=[following_id])


class Block(Base, BaseMixin):
    """User blocked another user."""

    __tablename__ = "blocks"

    blocker_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    blocked_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    # Relationships
    blocker: Mapped["User"] = relationship("User", foreign_keys=[blocker_id])
    blocked: Mapped["User"] = relationship("User", foreign_keys=[blocked_id])
