from sqlalchemy import Column, ForeignKey, Float
from db.base import Base
from models.base import BaseMixin


class Feed(Base, BaseMixin):
    """AI ranked feed cache."""
    __tablename__ = "feeds"

    user_id = Column(ForeignKey("users.id"), nullable=False)
    post_id = Column(ForeignKey("posts.id"), nullable=False)
    score = Column(Float)
