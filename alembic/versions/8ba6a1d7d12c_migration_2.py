"""migration 2

Revision ID: 8ba6a1d7d12c
Revises: dabd564f1676
Create Date: 2024-09-25 09:28:25.081623

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8ba6a1d7d12c'
down_revision: Union[str, None] = 'dabd564f1676'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
