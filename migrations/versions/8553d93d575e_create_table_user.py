"""Create table user

Revision ID: 8553d93d575e
Revises: 19f54b938643
Create Date: 2022-07-16 00:47:35.590345

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8553d93d575e'
down_revision = '19f54b938643'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
