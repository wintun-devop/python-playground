"""user_model_add

Revision ID: 32b11d44c79e
Revises: 49d914fd4812
Create Date: 2024-01-21 17:25:04.740658

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '32b11d44c79e'
down_revision: Union[str, None] = '49d914fd4812'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('profile', sa.String(), nullable=False),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.add_column('product', sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=False))
    op.add_column('product', sa.Column('updated', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'updated')
    op.drop_column('product', 'created')
    op.drop_table('user')
    # ### end Alembic commands ###
