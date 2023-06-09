"""empty message

Revision ID: 027688d2aaa4
Revises: f0f8da9c4e67
Create Date: 2023-04-25 20:32:55.788682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '027688d2aaa4'
down_revision = 'f0f8da9c4e67'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wolves',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('title', sa.String(length=140), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wolves')
    # ### end Alembic commands ###
