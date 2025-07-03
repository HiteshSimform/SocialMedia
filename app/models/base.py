from datetime import datetime
from sqlalchemy import Column, DateTime, Boolean, ForeignKey, Float, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import uuid
from typing import Optional


# Mixin for timestamps (created_at, updated_at)
class TimestampMixin:
    """Adds created_at and updated_at timestamps."""

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), onupdate=func.now()
    )


# Mixin for soft delete functionality (is_deleted, deleted_at)
class SoftDeleteMixin:
    """Adds soft delete support."""

    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)
    deleted_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))


# Mixin for UUID-based primary key
class IDMixin:
    """UUID-based primary key."""

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )


# Reusable base model that includes all mixins
class BaseMixin(IDMixin, TimestampMixin, SoftDeleteMixin):
    """Reusable base model."""

    pass
