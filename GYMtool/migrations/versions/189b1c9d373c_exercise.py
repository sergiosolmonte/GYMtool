"""exercise

Revision ID: 189b1c9d373c
Revises: ffdfe694adfd
Create Date: 2020-11-16 12:47:27.163146

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '189b1c9d373c'
down_revision = 'ffdfe694adfd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('exercise', sa.Column('description', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('exercise', 'description')
    # ### end Alembic commands ###
