"""Initial migration

Revision ID: cd958a21b209
Revises: 
Create Date: 2025-04-06 21:03:37.473299

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd958a21b209'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.TEXT(),
               type_=sa.String(length=200),
               existing_nullable=True)
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])
        batch_op.drop_column('completed')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('completed', sa.BOOLEAN(), nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('description',
               existing_type=sa.String(length=200),
               type_=sa.TEXT(),
               existing_nullable=True)

    # ### end Alembic commands ###
