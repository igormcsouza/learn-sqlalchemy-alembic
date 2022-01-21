"""Add column to the user table

Revision ID: 86feaea380dc
Revises: 1769bd47a4fe
Create Date: 2022-01-21 15:53:46.581494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86feaea380dc'
down_revision = '1769bd47a4fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('last_name', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_name')
    # ### end Alembic commands ###
