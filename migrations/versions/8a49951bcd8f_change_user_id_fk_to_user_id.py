"""Change user_id_fk to user_id

Revision ID: 8a49951bcd8f
Revises: 2365f19dd4f4
Create Date: 2021-08-14 08:20:05.461953

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a49951bcd8f'
down_revision = '2365f19dd4f4'
branch_labels = None
depends_on = None


def upgrade():
    # Start by dropping the constraint
    op.drop_constraint('posts_user_id_fk_fkey', 'posts', type_='foreignkey')
    # Then ALTER the column (don't drop!)
    op.alter_column(
        'posts', 'user_id_fk', nullable=False, new_column_name='user_id')
    # Then create the foreign key again.
    op.create_foreign_key(None, 'posts', 'users', ['user_id'], ['id'])

def downgrade():
    op.drop_constraint('posts_user_id_fkey', 'posts', type_='foreignkey')
    op.alter_column(
        'posts', 'user_id', nullable=False, new_column_name='user_id_fk')
    op.create_foreign_key(None, 'posts', 'users', ['user_id_fk'], ['id'])
