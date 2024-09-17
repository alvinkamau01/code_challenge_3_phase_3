"""Initial migration

Revision ID: dabd564f1676
Revises: 
Create Date: 2024-09-17 10:11:47.787614

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dabd564f1676'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bands',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('hometown', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('venues',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('city', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('concerts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('band_id', sa.Integer(), nullable=True),
    sa.Column('venue_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['band_id'], ['bands.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['venues.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('concerts')
    op.drop_table('venues')
    op.drop_table('bands')
    # ### end Alembic commands ###
