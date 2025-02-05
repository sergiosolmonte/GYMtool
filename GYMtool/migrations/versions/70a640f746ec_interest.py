"""interest

Revision ID: 70a640f746ec
Revises: 6d16adb83fd5
Create Date: 2020-11-17 12:30:49.842981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70a640f746ec'
down_revision = '6d16adb83fd5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('interest',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_interest_name'), 'interest', ['name'], unique=True)
    op.create_table('user_interest',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('interest_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['interest_id'], ['interest.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_interest')
    op.drop_index(op.f('ix_interest_name'), table_name='interest')
    op.drop_table('interest')
    # ### end Alembic commands ###
