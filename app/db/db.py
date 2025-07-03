from core.config import settings
from db.base import Base
from db.session import engine


def get_active_engine():
    return engine


def create_all_tables():
    """
    The function `create_all_tables` creates all tables defined in the metadata using the active engine.
    """
    engine = get_active_engine()
    Base.metadata.create_all(bind=engine)
