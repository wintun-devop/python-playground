from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String,Text,func
import uuid
import datetime

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "product"
    id:Mapped[str] = mapped_column(String(36),primary_key=True, default=uuid.uuid4())
    name:Mapped[str] = mapped_column(String(255),nullable=False)
    model_no:Mapped[str] = mapped_column(String(255),nullable=False, unique=True)
    description:Mapped[str] = mapped_column(Text,nullable=False)
    created: Mapped[datetime.datetime] = mapped_column(default=func.now())
    updated: Mapped[datetime.datetime] = mapped_column(nullable=True,onupdate=func.now())