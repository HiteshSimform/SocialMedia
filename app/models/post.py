from sqlalchemy import Column, ForeignKey, Text, Boolean, String, Integer
from sqlalchemy.orm import relationship
from db.base import Base
from models.base import BaseMixin


class Post(Base, BaseMixin):
    """Post created by users."""
    __tablename__ = "posts"

    user_id = Column(ForeignKey("users.id"), nullable=False)
    caption = Column(Text)
    is_private = Column(Boolean, default=False)

    user = relationship("User", back_populates="posts")
    media = relationship("PostMedia", back_populates="post", cascade="all, delete-orphan")


class PostMedia(Base, BaseMixin):
    """Attached media for posts."""
    __tablename__ = "post_media"

    post_id = Column(ForeignKey("posts.id"), nullable=False)
    media_url = Column(String(255), nullable=False)
    media_type = Column(String(10))  # image, video
    order_index = Column(Integer, default=0)

    post = relationship("Post", back_populates="media")
