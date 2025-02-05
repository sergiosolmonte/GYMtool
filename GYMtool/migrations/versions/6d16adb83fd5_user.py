"""user

Revision ID: 6d16adb83fd5
Revises: 189b1c9d373c
Create Date: 2020-11-17 12:13:36.457994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d16adb83fd5'
down_revision = '189b1c9d373c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('birthdate', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('height', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('weight', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'weight')
    op.drop_column('user', 'height')
    op.drop_column('user', 'birthdate')
    # ### end Alembic commands ###
