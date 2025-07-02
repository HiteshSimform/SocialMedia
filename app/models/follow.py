from sqlalchemy import Column, ForeignKey, String
from db.base import Base
from models.base import BaseMixin


class Follow(Base, BaseMixin):
    """Follow relationship."""
    __tablename__ = "follows"

    follower_id = Column(ForeignKey("users.id"), nullable=False)
    following_id = Column(ForeignKey("users.id"), nullable=False)
    status = Column(String(10), default="accepted")  # or 'pending'


class Block(Base, BaseMixin):
    """User blocked another user."""
    __tablename__ = "blocks"

    blocker_id = Column(ForeignKey("users.id"), nullable=False)
    blocked_id = Column(ForeignKey("users.id"), nullable=False)
