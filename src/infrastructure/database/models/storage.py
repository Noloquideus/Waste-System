import uuid
from sqlalchemy import Computed
from sqlalchemy.dialects.postgresql import UUID, VARCHAR, INTEGER
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.infrastructure.database.models.base import Base

class Storage(Base):
    __tablename__ = 'storage'

    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4())
    name: Mapped[str] = mapped_column(VARCHAR, nullable=False)
    biowaste: Mapped[int] = mapped_column(INTEGER, default=0)
    plastic: Mapped[int] = mapped_column(INTEGER, default=0)
    glass: Mapped[int] = mapped_column(INTEGER, default=0)
    biowaste_capacity: Mapped[int] = mapped_column(INTEGER, default=0)
    plastic_capacity: Mapped[int] = mapped_column(INTEGER, default=0)
    glass_capacity: Mapped[int] = mapped_column(INTEGER, default=0)
    biowaste_remaining: Mapped[int] = mapped_column(
        INTEGER, Computed('GREATEST(biowaste_capacity - biowaste, 0)')
    )
    plastic_remaining: Mapped[int] = mapped_column(
        INTEGER, Computed('GREATEST(plastic_capacity - plastic, 0)')
    )
    glass_remaining: Mapped[int] = mapped_column(
        INTEGER, Computed('GREATEST(glass_capacity - glass, 0)')
    )

    waste_transfers = relationship('WasteTransfer', back_populates='storage')
