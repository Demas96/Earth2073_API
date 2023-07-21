"""add scenes

Revision ID: eb13028e0406
Revises: b7cddd82b400
Create Date: 2023-07-21 23:42:41.512513

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb13028e0406'
down_revision = 'b7cddd82b400'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'scenes', ['name'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'scenes', type_='unique')
    # ### end Alembic commands ###