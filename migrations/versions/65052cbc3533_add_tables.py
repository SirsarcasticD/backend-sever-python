"""Add tables

Revision ID: 65052cbc3533
Revises: 
Create Date: 2022-11-22 12:45:14.703341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65052cbc3533'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('country',
    sa.Column('country_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('country_name', sa.String(length=50), nullable=False),
    sa.Column('code', sa.String(length=3), nullable=False),
    sa.Column('population', sa.INTEGER(), nullable=False),
    sa.Column('continent', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('country_id', name=op.f('pk_country'))
    )
    op.create_table('language',
    sa.Column('language_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('language', sa.String(length=20), nullable=False),
    sa.Column('created_on_utc', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('language_id', name=op.f('pk_language')),
    sa.UniqueConstraint('language_id', name=op.f('uq_language_language_id'))
    )
    op.create_table('option',
    sa.Column('option_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('option_content', sa.String(length=50), nullable=False),
    sa.Column('created_on_utc', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('option_id', name=op.f('pk_option')),
    sa.UniqueConstraint('option_id', name=op.f('uq_option_option_id'))
    )
    op.create_table('polltopic',
    sa.Column('polltopic_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('topic', sa.String(length=50), nullable=False),
    sa.Column('created_on_utc', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('polltopic_id', name=op.f('pk_polltopic')),
    sa.UniqueConstraint('polltopic_id', name=op.f('uq_polltopic_polltopic_id'))
    )
    op.create_table('region',
    sa.Column('region_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('region_name', sa.String(length=50), nullable=False),
    sa.Column('latitude', sa.DECIMAL(), nullable=False),
    sa.Column('longitude', sa.DECIMAL(), nullable=False),
    sa.Column('code', sa.String(length=3), nullable=False),
    sa.Column('country_id', sa.INTEGER(), nullable=False),
    sa.Column('region_type', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['country_id'], ['country.country_id'], name=op.f('fk_region_country_id_country')),
    sa.PrimaryKeyConstraint('region_id', name=op.f('pk_region'))
    )
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=20), nullable=False),
    sa.Column('region_id', sa.Integer(), nullable=False),
    sa.Column('country_id', sa.Integer(), nullable=False),
    sa.Column('dob', sa.Date(), nullable=False),
    sa.Column('key', sa.String(), nullable=True),
    sa.Column('last_time_active', sa.DateTime(), nullable=True),
    sa.Column('created_on_utc', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['country_id'], ['country.country_id'], name=op.f('fk_user_country_id_country')),
    sa.ForeignKeyConstraint(['region_id'], ['region.region_id'], name=op.f('fk_user_region_id_region')),
    sa.PrimaryKeyConstraint('user_id', name=op.f('pk_user')),
    sa.UniqueConstraint('email', name=op.f('uq_user_email')),
    sa.UniqueConstraint('user_id', name=op.f('uq_user_user_id')),
    sa.UniqueConstraint('username', name=op.f('uq_user_username'))
    )
    op.create_table('poll',
    sa.Column('poll_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('poll_title', sa.String(length=50), nullable=False),
    sa.Column('poll_content', sa.String(length=300), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('polltopic_id', sa.Integer(), nullable=True),
    sa.Column('language_id', sa.Integer(), nullable=True),
    sa.Column('created_on_utc', sa.DateTime(), nullable=False),
    sa.Column('modified_on_utc', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['language_id'], ['language.language_id'], name=op.f('fk_poll_language_id_language')),
    sa.ForeignKeyConstraint(['polltopic_id'], ['polltopic.polltopic_id'], name=op.f('fk_poll_polltopic_id_polltopic')),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], name=op.f('fk_poll_user_id_user')),
    sa.PrimaryKeyConstraint('poll_id', name=op.f('pk_poll')),
    sa.UniqueConstraint('poll_id', name=op.f('uq_poll_poll_id'))
    )
    op.create_index(op.f('ix_poll_user_id'), 'poll', ['user_id'], unique=False)
    op.create_table('comment',
    sa.Column('comment_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('comment_content', sa.String(length=50), nullable=False),
    sa.Column('poll_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('parent_comment_id', sa.Integer(), nullable=True),
    sa.Column('language_id', sa.Integer(), nullable=True),
    sa.Column('created_on_utc', sa.DateTime(), nullable=False),
    sa.Column('modified_on_utc', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['language_id'], ['language.language_id'], name=op.f('fk_comment_language_id_language')),
    sa.ForeignKeyConstraint(['parent_comment_id'], ['comment.comment_id'], name=op.f('fk_comment_parent_comment_id_comment')),
    sa.ForeignKeyConstraint(['poll_id'], ['poll.poll_id'], name=op.f('fk_comment_poll_id_poll')),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], name=op.f('fk_comment_user_id_user')),
    sa.PrimaryKeyConstraint('comment_id', name=op.f('pk_comment')),
    sa.UniqueConstraint('comment_id', name=op.f('uq_comment_comment_id'))
    )
    op.create_index(op.f('ix_comment_poll_id'), 'comment', ['poll_id'], unique=False)
    op.create_index(op.f('ix_comment_user_id'), 'comment', ['user_id'], unique=False)
    op.create_table('polloption',
    sa.Column('polloption_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('option_id', sa.Integer(), nullable=False),
    sa.Column('poll_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['option_id'], ['option.option_id'], name=op.f('fk_polloption_option_id_option')),
    sa.ForeignKeyConstraint(['poll_id'], ['poll.poll_id'], name=op.f('fk_polloption_poll_id_poll')),
    sa.PrimaryKeyConstraint('polloption_id', name=op.f('pk_polloption')),
    sa.UniqueConstraint('polloption_id', name=op.f('uq_polloption_polloption_id'))
    )
    op.create_table('pollsentiment',
    sa.Column('pollsentiment_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('poll_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('sentiment', sa.Integer(), nullable=False),
    sa.Column('created_on_utc', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['poll_id'], ['poll.poll_id'], name=op.f('fk_pollsentiment_poll_id_poll')),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], name=op.f('fk_pollsentiment_user_id_user')),
    sa.PrimaryKeyConstraint('pollsentiment_id', name=op.f('pk_pollsentiment')),
    sa.UniqueConstraint('pollsentiment_id', name=op.f('uq_pollsentiment_pollsentiment_id'))
    )
    op.create_index(op.f('ix_pollsentiment_poll_id'), 'pollsentiment', ['poll_id'], unique=False)
    op.create_index(op.f('ix_pollsentiment_user_id'), 'pollsentiment', ['user_id'], unique=False)
    op.create_table('shift',
    sa.Column('shift_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('comment_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('previous_polloption_id', sa.Integer(), nullable=False),
    sa.Column('new_polloption_id', sa.Integer(), nullable=False),
    sa.Column('created_on_utc', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['comment_id'], ['comment.comment_id'], name=op.f('fk_shift_comment_id_comment')),
    sa.ForeignKeyConstraint(['new_polloption_id'], ['polloption.polloption_id'], name=op.f('fk_shift_new_polloption_id_polloption')),
    sa.ForeignKeyConstraint(['previous_polloption_id'], ['polloption.polloption_id'], name=op.f('fk_shift_previous_polloption_id_polloption')),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], name=op.f('fk_shift_user_id_user')),
    sa.PrimaryKeyConstraint('shift_id', name=op.f('pk_shift')),
    sa.UniqueConstraint('shift_id', name=op.f('uq_shift_shift_id'))
    )
    op.create_index(op.f('ix_shift_new_polloption_id'), 'shift', ['new_polloption_id'], unique=False)
    op.create_index(op.f('ix_shift_user_id'), 'shift', ['user_id'], unique=False)
    op.create_table('vote',
    sa.Column('vote_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('polloption_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('region_id', sa.Integer(), nullable=False),
    sa.Column('country_id', sa.Integer(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('previous_vote_id', sa.Integer(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('created_on_utc', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['country_id'], ['country.country_id'], name=op.f('fk_vote_country_id_country')),
    sa.ForeignKeyConstraint(['polloption_id'], ['polloption.polloption_id'], name=op.f('fk_vote_polloption_id_polloption')),
    sa.ForeignKeyConstraint(['previous_vote_id'], ['vote.vote_id'], name=op.f('fk_vote_previous_vote_id_vote')),
    sa.ForeignKeyConstraint(['region_id'], ['region.region_id'], name=op.f('fk_vote_region_id_region')),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], name=op.f('fk_vote_user_id_user')),
    sa.PrimaryKeyConstraint('vote_id', name=op.f('pk_vote')),
    sa.UniqueConstraint('vote_id', name=op.f('uq_vote_vote_id'))
    )
    op.create_index(op.f('ix_vote_polloption_id'), 'vote', ['polloption_id'], unique=False)
    op.create_index(op.f('ix_vote_user_id'), 'vote', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_vote_user_id'), table_name='vote')
    op.drop_index(op.f('ix_vote_polloption_id'), table_name='vote')
    op.drop_table('vote')
    op.drop_index(op.f('ix_shift_user_id'), table_name='shift')
    op.drop_index(op.f('ix_shift_new_polloption_id'), table_name='shift')
    op.drop_table('shift')
    op.drop_index(op.f('ix_pollsentiment_user_id'), table_name='pollsentiment')
    op.drop_index(op.f('ix_pollsentiment_poll_id'), table_name='pollsentiment')
    op.drop_table('pollsentiment')
    op.drop_table('polloption')
    op.drop_index(op.f('ix_comment_user_id'), table_name='comment')
    op.drop_index(op.f('ix_comment_poll_id'), table_name='comment')
    op.drop_table('comment')
    op.drop_index(op.f('ix_poll_user_id'), table_name='poll')
    op.drop_table('poll')
    op.drop_table('user')
    op.drop_table('region')
    op.drop_table('polltopic')
    op.drop_table('option')
    op.drop_table('language')
    op.drop_table('country')
    # ### end Alembic commands ###
