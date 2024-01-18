from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import func

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "product"
    id:Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=func.uuid_generate_v4())
    name:Mapped[str] = mapped_column(nullable=False)
    model_no:Mapped[str] = mapped_column(nullable=False, unique=True)
    description:Mapped[str] = mapped_column(nullable=False)
    

    

    
