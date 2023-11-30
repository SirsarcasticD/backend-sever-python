"""Add countries

Revision ID: e1461dc09cfb
Revises: b5767183598c
Create Date: 2022-11-22 12:47:57.207735

"""
from alembic import op
import sqlalchemy as sa
from extract_countries_script import add_countries
# revision identifiers, used by Alembic.
revision = 'e1461dc09cfb'
down_revision = 'b5767183598c'
branch_labels = None
depends_on = None


def upgrade():

    add_countries()


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
