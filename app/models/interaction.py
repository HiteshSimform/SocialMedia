from sqlalchemy import Column, ForeignKey, Text
from db.base import Base
from models.base import BaseMixin
from sqlalchemy.orm import relationship


class Like(Base, BaseMixin):
    """Like on a post."""
    __tablename__ = "likes"

    user_id = Column(ForeignKey("users.id"), nullable=False)
    post_id = Column(ForeignKey("posts.id"), nullable=False)


class Comment(Base, BaseMixin):
    """User comment on a post."""
    __tablename__ = "comments"

    user_id = Column(ForeignKey("users.id"), nullable=False)
    post_id = Column(ForeignKey("posts.id"), nullable=False)
    parent_id = Column(ForeignKey("comments.id"), nullable=True)
    content = Column(Text, nullable=False)


class SavedPost(Base, BaseMixin):
    """User saved a post."""
    __tablename__ = "saved_posts"

    user_id = Column(ForeignKey("users.id"), nullable=False)
    post_id = Column(ForeignKey("posts.id"), nullable=False)
