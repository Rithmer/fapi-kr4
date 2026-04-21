"""add description to products

Revision ID: 20260421_03
Revises: 20260421_02
Create Date: 2026-04-21 00:10:00
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "20260421_03"
down_revision: Union[str, Sequence[str], None] = "20260421_02"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "products",
        sa.Column("description", sa.String(length=500), nullable=False, server_default="No description"),
    )


def downgrade() -> None:
    op.drop_column("products", "description")
