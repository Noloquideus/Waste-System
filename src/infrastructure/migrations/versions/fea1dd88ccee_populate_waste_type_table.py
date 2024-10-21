"""populate waste_type table

Revision ID: fea1dd88ccee
Revises: 1bc957466c3d
Create Date: 2024-10-20 03:41:51.116188

"""
import uuid
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import MetaData, Table

# revision identifiers, used by Alembic.
revision: str = 'fea1dd88ccee'
down_revision: Union[str, None] = '1bc957466c3d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    metadata = MetaData()

    waste_type_table = Table('waste_type', metadata, autoload_with=op.get_bind())

    op.bulk_insert(
        waste_type_table,
        [
            {'id': uuid.uuid4(), 'name': 'biowaste'},
            {'id': uuid.uuid4(), 'name': 'plastic'},
            {'id': uuid.uuid4(), 'name': 'glass'}
        ]
    )

def downgrade() -> None:
    op.execute("DELETE FROM waste_type WHERE name IN ('biowaste', 'plastic', 'glass')")
