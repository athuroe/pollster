"""created results table

Revision ID: 32b9be8971cb
Revises: 
Create Date: 2020-03-02 23:21:39.547078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32b9be8971cb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('result',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location', sa.Text(), nullable=True),
    sa.Column('question', sa.Text(), nullable=True),
    sa.Column('happy_count', sa.Integer(), nullable=True),
    sa.Column('sad_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('result')
    # ### end Alembic commands ###