from sqlalchemy import Column, String, ForeignKey
from db.base import Base
from models.base import BaseMixin


class Hashtag(Base, BaseMixin):
    """Hashtag used in post caption."""
    __tablename__ = "hashtags"

    name = Column(String(100), unique=True, nullable=False)
    usage_count = Column(String, default=0)


class PostHashtag(Base, BaseMixin):
    """Join table for hashtags and posts."""
    __tablename__ = "post_hashtags"

    post_id = Column(ForeignKey("posts.id"), nullable=False)
    hashtag_id = Column(ForeignKey("hashtags.id"), nullable=False)
