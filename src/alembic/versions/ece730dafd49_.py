"""empty message

Revision ID: ece730dafd49
Revises: 2ad2c2e8398e
Create Date: 2025-04-08 13:08:08.867662

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'ece730dafd49'
down_revision: Union[str, None] = '2ad2c2e8398e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Table', 'location',
               existing_type=postgresql.ENUM('hall', 'terrace', 'vip_hall', name='places'),
               type_=sa.Enum('hall', 'terrace', 'vip_hall', name='places', native_enum=False),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Table', 'location',
               existing_type=sa.Enum('hall', 'terrace', 'vip_hall', name='places', native_enum=False),
               type_=postgresql.ENUM('hall', 'terrace', 'vip_hall', name='places'),
               existing_nullable=False)
    # ### end Alembic commands ###
