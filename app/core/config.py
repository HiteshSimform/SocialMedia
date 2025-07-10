from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    LOG_LEVEL: str = "INFO"
    ALGORITHM: str
    SECRET_KEY: str

    class Config:
        env_file = "/home/hitesh.jethava@simform.dom/Desktop/Training/FastAPI-Project/SocialMedia/app/.env"


settings = Settings()
