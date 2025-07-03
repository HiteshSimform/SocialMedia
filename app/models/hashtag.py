from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from typing import List
from db.base import Base
from models.base import BaseMixin
import uuid


class Hashtag(Base, BaseMixin):
    """
    Represents a hashtag used in a post caption or comment.

    Attributes:
        name (str): The hashtag text (e.g., "#fitness").
        usage_count (int): Number of times the hashtag has been used.
    """

    __tablename__ = "hashtags"

    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    usage_count: Mapped[int] = mapped_column(default=0)

    posts: Mapped[List["PostHashtag"]] = relationship(
        back_populates="hashtag", cascade="all, delete-orphan"
    )


class PostHashtag(Base, BaseMixin):
    """
    Join table connecting posts and hashtags (many-to-many).

    Attributes:
        post_id (UUID): Reference to the post.
        hashtag_id (UUID): Reference to the hashtag.
    """

    __tablename__ = "post_hashtags"

    post_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("posts.id"), nullable=False)
    hashtag_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("hashtags.id"), nullable=False
    )

    hashtag: Mapped["Hashtag"] = relationship(back_populates="posts")
