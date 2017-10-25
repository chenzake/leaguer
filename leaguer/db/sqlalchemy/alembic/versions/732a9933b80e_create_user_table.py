"""Create user table

Revision ID: 732a9933b80e
Revises: 
Create Date: 2017-07-26 22:17:08.497479

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '732a9933b80e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(64), nullable=False, unique=True),
        sa.Column('email', sa.String(255)),
        sa.Column('numbers', sa.Integer),
        sa.Column('address', sa.String(120)),
        sa.Column('phonenumber', sa.String(120)),
        )

def downgrade():
    op.drop_table('user')