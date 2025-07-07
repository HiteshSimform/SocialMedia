"""
Permission keys used for RBAC in the system.
Each key follows the format: <module>.<action>
"""

# Auth / System
AUTH_REGISTER = "auth.register"
AUTH_LOGIN = "auth.login"
AUTH_VERIFY_EMAIL = "auth.verify_email"
USER_ASSIGN_ROLE = "user.assign_role"

# Users
USER_VIEW_PROFILE = "user.view_profile"
USER_EDIT_OWN_PROFILE = "user.edit_own_profile"
USER_VIEW_ANY_PROFILE = "user.view_any_profile"
USER_BLOCK_USER = "user.block_user"
USER_DELETE_USER = "user.delete_user"

# Posts
POST_CREATE = "post.create"
POST_EDIT_OWN = "post.edit_own"
POST_DELETE_OWN = "post.delete_own"
POST_DELETE_ANY = "post.delete_any"
POST_VIEW_PUBLIC = "post.view_public"
POST_VIEW_PRIVATE = "post.view_private"

# Comments
COMMENT_CREATE = "comment.create"
COMMENT_DELETE_OWN = "comment.delete_own"
COMMENT_DELETE_ANY = "comment.delete_any"

# Likes
LIKE_CREATE = "like.create"
LIKE_DELETE = "like.delete"

# Follows
FOLLOW_CREATE = "follow.create"
FOLLOW_DELETE = "follow.delete"

# Saved Posts
SAVE_CREATE = "save.create"
SAVE_DELETE = "save.delete"

# Hashtags
HASHTAG_VIEW = "hashtag.view"
HASHTAG_DELETE = "hashtag.delete"

# Stories
STORY_CREATE = "story.create"
STORY_DELETE_OWN = "story.delete_own"
STORY_DELETE_ANY = "story.delete_any"

# Reports
REPORT_CREATE = "report.create"
REPORT_VIEW = "report.view"
REPORT_RESOLVE = "report.resolve"

# Notifications
NOTIFICATION_VIEW = "notification.view"
NOTIFICATION_READ = "notification.read"

# Admin
ADMIN_PANEL_ACCESS = "admin.panel.access"
ADMIN_VIEW_AUDIT_LOGS = "admin.view_audit_logs"

# All permissions in one list (for seeding or export)
ALL_PERMISSIONS = [
    # Auth
    AUTH_REGISTER,
    AUTH_LOGIN,
    AUTH_VERIFY_EMAIL,
    USER_ASSIGN_ROLE,
    # Users
    USER_VIEW_PROFILE,
    USER_EDIT_OWN_PROFILE,
    USER_VIEW_ANY_PROFILE,
    USER_BLOCK_USER,
    USER_DELETE_USER,
    # Posts
    POST_CREATE,
    POST_EDIT_OWN,
    POST_DELETE_OWN,
    POST_DELETE_ANY,
    POST_VIEW_PUBLIC,
    POST_VIEW_PRIVATE,
    # Comments
    COMMENT_CREATE,
    COMMENT_DELETE_OWN,
    COMMENT_DELETE_ANY,
    # Likes
    LIKE_CREATE,
    LIKE_DELETE,
    # Follows
    FOLLOW_CREATE,
    FOLLOW_DELETE,
    # Saved
    SAVE_CREATE,
    SAVE_DELETE,
    # Hashtag
    HASHTAG_VIEW,
    HASHTAG_DELETE,
    # Stories
    STORY_CREATE,
    STORY_DELETE_OWN,
    STORY_DELETE_ANY,
    # Reports
    REPORT_CREATE,
    REPORT_VIEW,
    REPORT_RESOLVE,
    # Notifications
    NOTIFICATION_VIEW,
    NOTIFICATION_READ,
    # Admin
    ADMIN_PANEL_ACCESS,
    ADMIN_VIEW_AUDIT_LOGS,
]
