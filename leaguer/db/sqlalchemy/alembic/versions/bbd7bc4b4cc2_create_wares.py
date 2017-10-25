"""create wares

Revision ID: bbd7bc4b4cc2
Revises: 732a9933b80e
Create Date: 2017-10-25 10:46:27.678000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bbd7bc4b4cc2'
down_revision = '732a9933b80e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'wares',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('name', sa.String),
        sa.Column('cost', sa.Float),
        sa.Column('price', sa.Float),
        sa.Column('preferential_price', sa.Float),
        sa.Column('create_time', sa.Date),
    )


def downgrade():
    op.drop_table('wares')
