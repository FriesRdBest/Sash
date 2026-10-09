"""Configuration layer for Sash."""

import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class Config:
    """Application configuration from environment variables."""
    
    # Database
    database_url: str = "sqlite:///sash.db"
    
    # Application
    app_name: str = "Sash"
    debug: bool = False
    
    # Mock mode
    mock_mode: bool = True
    
    # Limits
    max_workflow_steps: int = 10
    max_retries: int = 3
    
    @classmethod
    def from_env(cls) -> "Config":
        """Load configuration from environment variables."""
        return cls(
            database_url=os.getenv("DATABASE_URL", "sqlite:///sash.db"),
            app_name=os.getenv("APP_NAME", "Sash"),
            debug=os.getenv("DEBUG", "false").lower() == "true",
            mock_mode=os.getenv("MOCK_MODE", "true").lower() == "true",
            max_workflow_steps=int(os.getenv("MAX_WORKFLOW_STEPS", "10")),
            max_retries=int(os.getenv("MAX_RETRIES", "3")),
        )


# Global config instance
config = Config.from_env()
