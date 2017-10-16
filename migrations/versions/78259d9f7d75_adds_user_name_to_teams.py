"""adds_user_name_to_teams

Revision ID: 78259d9f7d75
Revises: cbf5620f8e15
Create Date: 2017-09-27 15:22:15.882646

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text


# revision identifiers, used by Alembic.
revision = '78259d9f7d75'
down_revision = 'cbf5620f8e15'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('teams', sa.Column('user_name', sa.VARCHAR(128), nullable=False, unique=True))
    conn = op.get_bind()
    conn.execute(text("UPDATE teams SET user_name = name"))


def downgrade():
    op.drop_column('challenges', 'user_name')
