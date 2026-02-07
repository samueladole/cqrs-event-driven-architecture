from pydantic_settings  import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./read_side/read_db.sqlite3"

settings = Settings()
