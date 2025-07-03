from sqlalchemy import ForeignKey, Float, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
import uuid
from db.base import Base
from models.base import BaseMixin


class Feed(Base, BaseMixin):
    """AI ranked feed cache."""

    __tablename__ = "feeds"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    post_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("posts.id"), nullable=False)
    score: Mapped[float] = mapped_column(Float)
