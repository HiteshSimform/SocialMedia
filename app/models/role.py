from sqlalchemy import Column, ForeignKey, String
from db.base import Base
from models.base import BaseMixin


class Role(Base, BaseMixin):
    """System role."""
    __tablename__ = "roles"

    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255))


class Permission(Base, BaseMixin):
    """System permission key."""
    __tablename__ = "permissions"

    key = Column(String(100), unique=True, nullable=False)
    description = Column(String(255))


class RolePermission(Base, BaseMixin):
    """Join between roles and permissions."""
    __tablename__ = "role_permissions"

    role_id = Column(ForeignKey("roles.id"), nullable=False)
    permission_id = Column(ForeignKey("permissions.id"), nullable=False)


class UserRole(Base, BaseMixin):
    """Assign role to user."""
    __tablename__ = "user_roles"

    user_id = Column(ForeignKey("users.id"), nullable=False)
    role_id = Column(ForeignKey("roles.id"), nullable=False)
