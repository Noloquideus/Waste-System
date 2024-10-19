import uuid
from sqlalchemy.dialects.postgresql import UUID, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column
from src.infrastructure.database.models.base import Base


class WasteType(Base):
    __tablename__ = 'waste_type'

    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4())
    name: Mapped[str] = mapped_column(VARCHAR, nullable=False, unique=True)
