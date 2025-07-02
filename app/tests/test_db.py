from db.session import SessionLocal

def test_db_connection():
    db = SessionLocal()
    result = db.execute("SELECT 1")
    assert result.scalar() == 1
    db.close()