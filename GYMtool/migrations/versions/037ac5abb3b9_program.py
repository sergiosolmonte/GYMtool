"""program

Revision ID: 037ac5abb3b9
Revises: 70a640f746ec
Create Date: 2020-11-18 16:36:12.912326

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '037ac5abb3b9'
down_revision = '70a640f746ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('program', sa.Column('name', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('program', 'name')
    # ### end Alembic commands ###
