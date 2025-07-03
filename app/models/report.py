from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey
from typing import Optional
from db.base import Base
from models.base import BaseMixin
import uuid


class Report(Base, BaseMixin):
    """
    Represents a content or user report submitted by a user.

    Attributes:
        reporter_id (UUID): The ID of the user submitting the report.
        target_type (str): Type of the entity being reported ('user', 'post', 'comment').
        target_id (str): ID of the reported entity (stored as string for generalization).
        reason (str): Reason for the report.
        status (str): Current status of the report ('pending', 'resolved', etc.).
        resolved_by (UUID): Admin or moderator who resolved the report.
    """

    __tablename__ = "reports"

    reporter_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"), nullable=False
    )
    target_type: Mapped[str] = mapped_column(
        String(20), nullable=False
    )  # e.g., 'user', 'post', 'comment'
    target_id: Mapped[str] = mapped_column(String(50), nullable=False)
    reason: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[str] = mapped_column(String(20), default="pending")
    resolved_by: Mapped[Optional[uuid.UUID]] = mapped_column(
        ForeignKey("users.id"), nullable=True
    )
