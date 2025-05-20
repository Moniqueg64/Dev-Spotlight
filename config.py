
import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "devspotlight-secret")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///devspotlight.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
