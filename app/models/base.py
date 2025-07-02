from sqlalchemy import Column, DateTime, Boolean, func
from sqlalchemy.dialects.postgresql import UUID
import uuid


class TimestampMixin:
    """Adds created_at and updated_at timestamps."""
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class SoftDeleteMixin:
    """Adds soft delete support."""
    is_deleted = Column(Boolean, default=False)
    deleted_at = Column(DateTime(timezone=True))


class IDMixin:
    """UUID-based primary key."""
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)


class BaseMixin(IDMixin, TimestampMixin, SoftDeleteMixin):
    """Reusable base model."""
    pass
