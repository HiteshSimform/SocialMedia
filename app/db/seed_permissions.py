from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from models.role import RolePermission, Role, Permission
from app.core import permissions as perm

ROLE_PERMISSIONS = {
    "admin": perm.ALL_PERMISSIONS,
    "moderator": [
        perm.AUTH_LOGIN,
        perm.AUTH_VERIFY_EMAIL,
        perm.USER_VIEW_PROFILE,
        perm.USER_EDIT_OWN_PROFILE,
        perm.USER_VIEW_ANY_PROFILE,
        perm.USER_BLOCK_USER,
        perm.POST_CREATE,
        perm.POST_EDIT_OWN,
        perm.POST_DELETE_OWN,
        perm.POST_DELETE_ANY,
        perm.POST_VIEW_PUBLIC,
        perm.POST_VIEW_PRIVATE,
        perm.COMMENT_CREATE,
        perm.COMMENT_DELETE_OWN,
        perm.COMMENT_DELETE_ANY,
        perm.LIKE_CREATE,
        perm.LIKE_DELETE,
        perm.FOLLOW_CREATE,
        perm.FOLLOW_DELETE,
        perm.SAVE_CREATE,
        perm.SAVE_DELETE,
        perm.HASHTAG_VIEW,
        perm.STORY_CREATE,
        perm.STORY_DELETE_OWN,
        perm.STORY_DELETE_ANY,
        perm.REPORT_VIEW,
        perm.REPORT_RESOLVE,
        perm.NOTIFICATION_VIEW,
        perm.NOTIFICATION_READ,
        perm.ADMIN_PANEL_ACCESS,
    ],
    "user": [
        perm.AUTH_REGISTER,
        perm.AUTH_LOGIN,
        perm.AUTH_VERIFY_EMAIL,
        perm.USER_VIEW_PROFILE,
        perm.USER_EDIT_OWN_PROFILE,
        perm.POST_CREATE,
        perm.POST_EDIT_OWN,
        perm.POST_DELETE_OWN,
        perm.POST_VIEW_PUBLIC,
        perm.POST_VIEW_PRIVATE,
        perm.COMMENT_CREATE,
        perm.COMMENT_DELETE_OWN,
        perm.LIKE_CREATE,
        perm.LIKE_DELETE,
        perm.FOLLOW_CREATE,
        perm.FOLLOW_DELETE,
        perm.SAVE_CREATE,
        perm.SAVE_DELETE,
        perm.HASHTAG_VIEW,
        perm.STORY_CREATE,
        perm.STORY_DELETE_OWN,
        perm.REPORT_CREATE,
        perm.NOTIFICATION_VIEW,
        perm.NOTIFICATION_READ,
    ],
}


async def seed_permissions_and_roles(session: AsyncSession) -> None:
    """Seed permissions and roles into the database."""

    # Insert permissions
    for key in perm.ALL_PERMISSIONS:
        exists = await session.scalar(select(Permission).where(Permission.key == key))
        if not exists:
            session.add(Permission(key=key, description=key.replace(".", " ").title()))

    await session.commit()

    for role_name, role_perms in ROLE_PERMISSIONS.items():
        role = await session.scalar(select(Role).where(Role.name == role_name))
        if not role:
            role = Role(name=role_name, description=f"{role_name.capitalize()} role")
            session.add(role)
            await session.flush()  # So role.id is available

        for perm_key in role_perms:
            permission = await session.scalar(
                select(Permission).where(Permission.key == perm_key)
            )
            if permission:
                # Check for existing RolePermission
                exists = await session.scalar(
                    select(RolePermission).where(
                        RolePermission.role_id == role.id,
                        RolePermission.permission_id == permission.id,
                    )
                )
                if not exists:
                    session.add(
                        RolePermission(role_id=role.id, permission_id=permission.id)
                    )

    await session.commit()
