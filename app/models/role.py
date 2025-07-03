from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey
from db.base import Base
from models.base import BaseMixin
import uuid


class Role(Base, BaseMixin):
    """
    Represents a system role (e.g., user, admin, moderator).

    Attributes:
        name (str): Unique name of the role.
        description (str): Optional description.
    """

    __tablename__ = "roles"

    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(255), default="")


class Permission(Base, BaseMixin):
    """
    Represents a permission that can be assigned to a role (e.g., 'delete_user').

    Attributes:
        key (str): Unique key identifier for the permission.
        description (str): Human-readable description.
    """

    __tablename__ = "permissions"

    key: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(255), default="")


class RolePermission(Base, BaseMixin):
    """
    Join table between roles and permissions.

    Attributes:
        role_id (UUID): Foreign key to a Role.
        permission_id (UUID): Foreign key to a Permission.
    """

    __tablename__ = "role_permissions"

    role_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("roles.id"), nullable=False)
    permission_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("permissions.id"), nullable=False
    )


class UserRole(Base, BaseMixin):
    """
    Assigns a role to a user.

    Attributes:
        user_id (UUID): ID of the user.
        role_id (UUID): ID of the role.
    """

    __tablename__ = "user_roles"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    role_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("roles.id"), nullable=False)
