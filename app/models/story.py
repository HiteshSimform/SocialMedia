from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, ForeignKey
from db.base import Base
from models.base import BaseMixin
import uuid
import datetime


class Story(Base, BaseMixin):
    """
    Represents a temporary user story (disappears after 24 hours).

    Attributes:
        user_id (UUID): The ID of the user who posted the story.
        media_url (str): The URL to the image/video content.
        expires_at (datetime): Timestamp when the story expires.
    """

    __tablename__ = "stories"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    media_url: Mapped[str] = mapped_column(String(255), nullable=False)
    expires_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )
