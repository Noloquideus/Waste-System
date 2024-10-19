import uuid
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID, INTEGER
from sqlalchemy.orm import relationship, mapped_column, Mapped
from src.infrastructure.database.models.base import Base


class WasteTransfer(Base):
    __tablename__ = 'waste_transfers'

    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4())
    organization_id: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey('organization.id'), nullable=False)
    storage_id: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey('storage.id'), nullable=False)
    waste_type_id: Mapped[uuid.UUID] = mapped_column(UUID, ForeignKey('waste_type.id'), nullable=False)
    quantity: Mapped[int] = mapped_column(INTEGER, nullable=False)

    organization = relationship('Organization', back_populates='waste_transfers')
    storage = relationship('Storage', back_populates='waste_transfers')
    waste_type = relationship('WasteType')
