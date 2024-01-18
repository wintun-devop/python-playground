from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String,Text
import uuid

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "product"
    id:Mapped[str] = mapped_column(String(36),primary_key=True, default=uuid.uuid4())
    name:Mapped[str] = mapped_column(String(255),nullable=False)
    model_no:Mapped[str] = mapped_column(String(255),nullable=False, unique=True)
    description:Mapped[str] = mapped_column(Text,nullable=False)
    
    