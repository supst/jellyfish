"""SQLAlchemy ORM 模型。"""

from app.core.db import Base
from app.models.base import TimestampMixin

__all__ = ["Base", "TimestampMixin"]
