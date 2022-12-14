"""add table contact

Revision ID: fd27324a4ccc
Revises: 5c373a40c7f2
Create Date: 2022-09-23 12:27:31.194697

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd27324a4ccc'
down_revision = '5c373a40c7f2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Contacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=55), nullable=False),
    sa.Column('value', sa.Text(), nullable=False),
    sa.Column('start_at', sa.DateTime(), nullable=True),
    sa.Column('end_at', sa.DateTime(), nullable=True),
    sa.Column('auth_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['auth_id'], ['auth.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Contacts_id'), 'Contacts', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Contacts_id'), table_name='Contacts')
    op.drop_table('Contacts')
    # ### end Alembic commands ###
