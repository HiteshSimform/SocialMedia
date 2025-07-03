# app/models/notification.py

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean, ForeignKey
from typing import Optional
from db.base import Base
from models.base import BaseMixin
import uuid


class Notification(Base, BaseMixin):
    """
    Represents a user-facing notification triggered by events such as likes, comments, or follows.

    Attributes:
        user_id (UUID): The user receiving the notification.
        source_user_id (UUID): The user who triggered the event.
        post_id (UUID): The related post, if applicable.
        comment_id (UUID): The related comment, if applicable.
        type (str): Type of notification (e.g., 'like', 'comment', 'mention', 'follow').
        is_read (bool): Whether the user has seen the notification.
    """

    __tablename__ = "notifications"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    source_user_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        ForeignKey("users.id"), nullable=True
    )
    post_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        ForeignKey("posts.id"), nullable=True
    )
    comment_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        ForeignKey("comments.id"), nullable=True
    )
    type: Mapped[str] = mapped_column(
        String(20), nullable=False
    )  # e.g. 'like', 'follow'
    is_read: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
