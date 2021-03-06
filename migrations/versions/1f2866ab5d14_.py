"""empty message

Revision ID: 1f2866ab5d14
Revises: 266c1c3f29b7
Create Date: 2017-12-14 14:27:22.812102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f2866ab5d14'
down_revision = '266c1c3f29b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('article', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('article', 'updated_at')
    op.drop_column('article', 'created_at')
    # ### end Alembic commands ###
