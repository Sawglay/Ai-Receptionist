from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    GOOGLE_CALENDAR_ID: str = "primary"
    LOG_LEVEL: str = "INFO"
    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()