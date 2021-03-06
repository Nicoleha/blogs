"""another Migration

Revision ID: 9495f0282683
Revises: 4341522cc73c
Create Date: 2019-03-04 09:46:16.240659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9495f0282683'
down_revision = '4341522cc73c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_subscribes_email', table_name='subscribes')
    op.drop_index('ix_subscribes_name', table_name='subscribes')
    op.create_unique_constraint(None, 'subscribes', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'subscribes', type_='unique')
    op.create_index('ix_subscribes_name', 'subscribes', ['name'], unique=False)
    op.create_index('ix_subscribes_email', 'subscribes', ['email'], unique=True)
    # ### end Alembic commands ###
