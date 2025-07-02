from sqlalchemy import Column, ForeignKey, String, DateTime
from db.base import Base
from models.base import BaseMixin


class Story(Base, BaseMixin):
    """User story (24h content)."""
    __tablename__ = "stories"

    user_id = Column(ForeignKey("users.id"), nullable=False)
    media_url = Column(String(255), nullable=False)
    expires_at = Column(DateTime(timezone=True), nullable=False)
