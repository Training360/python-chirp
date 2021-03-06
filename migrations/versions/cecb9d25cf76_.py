"""empty message

Revision ID: cecb9d25cf76
Revises: e71d0f9f17c8
Create Date: 2021-03-15 15:27:47.894620

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cecb9d25cf76'
down_revision = 'e71d0f9f17c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('video_url', sa.String(length=250), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'video_url')
    # ### end Alembic commands ###
