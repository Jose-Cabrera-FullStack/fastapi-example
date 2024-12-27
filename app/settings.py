from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    db_url: str = Field("sqlite:///test.db", env='DATABASE_URL')


settings = Settings()
