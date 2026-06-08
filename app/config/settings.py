from pydantic_settings import BaseSettings
from typing import List
import urllib.parse

class Settings(BaseSettings):
    APP_NAME: str = "SuperMarket_Management_System"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    SECRET_KEY: str = "super-market-secret-jwt-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440

    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "Puncha@2006"
    DB_NAME: str = "supermarketdb"

    ALLOWED_ORIGINS: str = "http://localhost:3000,http://localhost:8080,http://127.0.0.1:5500"

    @property
    def DATABASE_URL(self) -> str:
        password = urllib.parse.quote_plus(self.DB_PASSWORD)

        return (
            f"postgresql+psycopg://{self.DB_USER}:{password}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    @property
    def CORS_ORIGINS(self) -> List[str]:
        return [origin.strip() for origin in self.ALLOWED_ORIGINS.split(",")]

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
