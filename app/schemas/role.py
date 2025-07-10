from uuid import UUID
from pydantic import BaseModel

class RoleAssignRequest(BaseModel):
    user_id: UUID
    role_name: str

class RoleResponse(BaseModel):
    id: UUID
    name: str
    description: str | None = None