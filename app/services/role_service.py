from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from app.models import UserRole, Role
from uuid import UUID
from fastapi import HTTPException, status
