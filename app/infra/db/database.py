from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import setting

DB_URL=f"postgresql://{setting.DB_USER}:{setting.DB_PASSWORD}@{setting.DB_HOST}:{setting.DB_PORT}/{setting.DB_NAME}"

engine=create_engine(DB_URL,echo=True)

sessionlocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)

def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()