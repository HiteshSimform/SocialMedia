from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text
from db.base import Base
from models.base import BaseMixin
from typing import Optional, List
import uuid


class Like(Base, BaseMixin):
    """
    Represents a like given by a user to a post.
    """

    __tablename__ = "likes"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    post_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("posts.id"), nullable=False)


class Comment(Base, BaseMixin):
    """
    Represents a comment made by a user on a post. Supports nesting via parent_id.
    """

    __tablename__ = "comments"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    post_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("posts.id"), nullable=False)
    parent_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        ForeignKey("comments.id"), nullable=True
    )
    content: Mapped[str] = mapped_column(Text, nullable=False)

    replies: Mapped[List["Comment"]] = relationship(
        backref="parent", remote_side="Comment.id", cascade="all, delete-orphan"
    )


class SavedPost(Base, BaseMixin):
    """
    Represents a post saved by a user to view later.
    """

    __tablename__ = "saved_posts"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    post_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("posts.id"), nullable=False)
