"""empty message

Revision ID: c3083ffc90ce
Revises: 
Create Date: 2020-04-26 07:41:08.955339

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3083ffc90ce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('page_info', sa.Column('theme', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('page_info', 'theme')
    # ### end Alembic commands ###
