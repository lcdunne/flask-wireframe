"""empty message

Revision ID: 8a57f129e0c6
Revises: 8a49951bcd8f
Create Date: 2021-08-14 18:43:35.088429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a57f129e0c6'
down_revision = '8a49951bcd8f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('newcol', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'newcol')
    # ### end Alembic commands ###
