"""seed two products

Revision ID: 20260421_02
Revises: 20260421_01
Create Date: 2026-04-21 00:05:00
"""

from typing import Sequence, Union

from alembic import op

revision: str = "20260421_02"
down_revision: Union[str, Sequence[str], None] = "20260421_01"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        INSERT INTO products (id, title, price, count)
        VALUES
            (1, 'Headphones', 99.99, 15),
            (2, 'Keyboard', 49.50, 20)
        """
    )


def downgrade() -> None:
    op.execute("DELETE FROM products WHERE id IN (1, 2)")
