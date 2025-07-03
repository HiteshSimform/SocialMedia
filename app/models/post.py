from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text, Boolean, String, Integer
from typing import Optional, List
from db.base import Base
from models.base import BaseMixin
import uuid
from models.user import User


class Post(Base, BaseMixin):
    """
    Represents a user's post, which may include one or more media items and a caption.
    """

    __tablename__ = "posts"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    caption: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    is_private: Mapped[bool] = mapped_column(Boolean, default=False)

    user: Mapped["User"] = relationship(back_populates="posts")
    media: Mapped[List["PostMedia"]] = relationship(
        back_populates="post",
        cascade="all, delete-orphan",
        order_by="PostMedia.order_index",
    )


class PostMedia(Base, BaseMixin):
    """
    Stores media files (image or video) associated with a post.
    """

    __tablename__ = "post_media"

    post_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("posts.id"), nullable=False)
    media_url: Mapped[str] = mapped_column(String(255), nullable=False)
    media_type: Mapped[str] = mapped_column(String(10))  # 'image', 'video'
    order_index: Mapped[int] = mapped_column(Integer, default=0)

    post: Mapped["Post"] = relationship(back_populates="media")
