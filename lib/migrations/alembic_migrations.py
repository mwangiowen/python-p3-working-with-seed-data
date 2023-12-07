# alembic_migrations.py

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'games',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=True),
        sa.Column('genre', sa.String(), nullable=True),
        sa.Column('platform', sa.String(), nullable=True),
        sa.Column('price', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('games')
