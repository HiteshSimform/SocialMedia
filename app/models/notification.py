from sqlalchemy import Column, ForeignKey, String, Boolean
from db.base import Base
from models.base import BaseMixin


class Notification(Base, BaseMixin):
    """In-app notification."""
    __tablename__ = "notifications"

    user_id = Column(ForeignKey("users.id"), nullable=False)
    source_user_id = Column(ForeignKey("users.id"), nullable=True)
    post_id = Column(ForeignKey("posts.id"), nullable=True)
    comment_id = Column(ForeignKey("comments.id"), nullable=True)
    type = Column(String(20))  # follow, like, comment, mention
    is_read = Column(Boolean, default=False)
