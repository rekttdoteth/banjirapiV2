"""empty message

Revision ID: 03b9cee4f337
Revises: 
Create Date: 2017-05-29 07:32:53.614156

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '03b9cee4f337'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('infobanjir_',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('state', sa.String(length=255), nullable=True),
    sa.Column('station_name', sa.String(length=255), nullable=True),
    sa.Column('district', sa.String(length=255), nullable=True),
    sa.Column('river_basin', sa.String(length=255), nullable=True),
    sa.Column('last_update', sa.DateTime(), nullable=True),
    sa.Column('water_level', sa.Float(asdecimal=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('info')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('info',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('state', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('station_name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('district', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('river_basin', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('last_update', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('water_level', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='info_pkey')
    )
    op.drop_table('infobanjir_')
    # ### end Alembic commands ###
