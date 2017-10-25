"""create profit and wares

Revision ID: 927da5f89216
Revises: bbd7bc4b4cc2
Create Date: 2017-10-25 14:54:33.818000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '927da5f89216'
down_revision = 'bbd7bc4b4cc2'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'sold_note',
        sa.Column('sold_id', sa.BigInteger, sa.ForeignKey('wares.id'), primary_key=True),
        sa.Column('sold_name', sa.String),
        sa.Column('sold_time', sa.DateTime),
        sa.Column('sold_num', sa.Integer),
        sa.Column('unit_price', sa.Float),
        sa.Column('total_cost', sa.Float),
        sa.Column('total_price', sa.Float),
    )

    op.create_table(
        'profits',
        sa.Column('date', sa.Date),
        sa.Column('price', sa.Float),
        sa.Column('cost', sa.Float),
        sa.Column('profit', sa.Float),

    )


def downgrade():
    op.drop_table('sold_note')
    op.drop_table('profits')