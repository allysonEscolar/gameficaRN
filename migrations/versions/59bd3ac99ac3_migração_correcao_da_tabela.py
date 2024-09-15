"""Migração correcao da tabela

Revision ID: 59bd3ac99ac3
Revises: afe56dbd7c95
Create Date: 2024-09-15 19:07:30.001572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59bd3ac99ac3'
down_revision = 'afe56dbd7c95'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('jogo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nomeJogo', sa.String(length=100), nullable=True),
    sa.Column('disciplina', sa.String(length=100), nullable=True),
    sa.Column('conteudo', sa.String(length=300), nullable=True),
    sa.Column('descricao', sa.String(length=500), nullable=True),
    sa.Column('link', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('jogo')
    # ### end Alembic commands ###
