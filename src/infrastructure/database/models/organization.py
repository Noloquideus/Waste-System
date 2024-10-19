import uuid
from sqlalchemy.dialects.postgresql import UUID, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.infrastructure.database.models.base import Base

class Organization(Base):
    __tablename__ = 'organization'

    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4())
    name: Mapped[str] = mapped_column(VARCHAR, nullable=False, unique=True)
    waste_transfers = relationship('WasteTransfer', back_populates='organization')
   