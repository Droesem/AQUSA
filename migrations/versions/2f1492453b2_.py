"""empty message

Revision ID: 2f1492453b2
Revises: 2f6f38df8ad
Create Date: 2015-05-11 10:13:36.960610

"""

# revision identifiers, used by Alembic.
revision = '2f1492453b2'
down_revision = '2f6f38df8ad'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('error', 'false_positive',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('error', 'false_positive',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    ### end Alembic commands ###