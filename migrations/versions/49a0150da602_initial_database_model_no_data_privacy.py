"""initial database model -- no data privacy

Revision ID: 49a0150da602
Revises: 
Create Date: 2022-08-20 00:31:34.743073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49a0150da602'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('journals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('content', sa.String(length=1000), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('journals')
    op.drop_table('users')
    # ### end Alembic commands ###
