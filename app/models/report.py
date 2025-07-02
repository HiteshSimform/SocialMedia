from sqlalchemy import Column, ForeignKey, String
from db.base import Base
from models.base import BaseMixin


class Report(Base, BaseMixin):
    """Content or user report."""
    __tablename__ = "reports"

    reporter_id = Column(ForeignKey("users.id"), nullable=False)
    target_type = Column(String(20))  # user, post, comment
    target_id = Column(String(50))
    reason = Column(String(255))
    status = Column(String(20), default="pending")
    resolved_by = Column(ForeignKey("users.id"), nullable=True)
