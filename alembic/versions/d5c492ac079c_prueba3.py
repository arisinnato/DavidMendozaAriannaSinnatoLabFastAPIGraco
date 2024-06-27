"""prueba3

Revision ID: d5c492ac079c
Revises: 277c9bbe63dc
Create Date: 2024-06-24 10:35:46.854428

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd5c492ac079c'
down_revision: Union[str, None] = '277c9bbe63dc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_productos_altura_cm', table_name='productos')
    op.drop_index('ix_productos_anchura_cm', table_name='productos')
    op.drop_index('ix_productos_descripcion', table_name='productos')
    op.drop_index('ix_productos_imagen', table_name='productos')
    op.drop_index('ix_productos_nombre', table_name='productos')
    op.drop_index('ix_productos_peso_gramo', table_name='productos')
    op.drop_index('ix_productos_profundidad_cm', table_name='productos')
    op.drop_table('productos')
    op.drop_index('ix_usuarios_apellidos', table_name='usuarios')
    op.drop_index('ix_usuarios_contraseña', table_name='usuarios')
    op.drop_index('ix_usuarios_correo', table_name='usuarios')
    op.drop_index('ix_usuarios_direccion', table_name='usuarios')
    op.drop_index('ix_usuarios_nacimiento', table_name='usuarios')
    op.drop_index('ix_usuarios_nombres', table_name='usuarios')
    op.drop_table('usuarios')
    op.drop_index('ix_tipos_productos_descripcion', table_name='tipos_productos')
    op.drop_index('ix_tipos_productos_funcionalidad', table_name='tipos_productos')
    op.drop_index('ix_tipos_productos_nombre', table_name='tipos_productos')
    op.drop_table('tipos_productos')
    op.drop_index('ix_tipos_usuarios_descripcion', table_name='tipos_usuarios')
    op.drop_index('ix_tipos_usuarios_nombre', table_name='tipos_usuarios')
    op.drop_table('tipos_usuarios')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tipos_usuarios',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('nombre', sa.VARCHAR(), nullable=True),
    sa.Column('descripcion', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_tipos_usuarios_nombre', 'tipos_usuarios', ['nombre'], unique=False)
    op.create_index('ix_tipos_usuarios_descripcion', 'tipos_usuarios', ['descripcion'], unique=False)
    op.create_table('tipos_productos',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('nombre', sa.VARCHAR(), nullable=True),
    sa.Column('descripcion', sa.VARCHAR(), nullable=True),
    sa.Column('funcionalidad', sa.BOOLEAN(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_tipos_productos_nombre', 'tipos_productos', ['nombre'], unique=False)
    op.create_index('ix_tipos_productos_funcionalidad', 'tipos_productos', ['funcionalidad'], unique=False)
    op.create_index('ix_tipos_productos_descripcion', 'tipos_productos', ['descripcion'], unique=False)
    op.create_table('usuarios',
    sa.Column('cedula', sa.VARCHAR(), nullable=False),
    sa.Column('nombres', sa.VARCHAR(), nullable=True),
    sa.Column('apellidos', sa.VARCHAR(), nullable=True),
    sa.Column('nacimiento', sa.DATETIME(), nullable=True),
    sa.Column('direccion', sa.VARCHAR(), nullable=True),
    sa.Column('correo', sa.VARCHAR(), nullable=True),
    sa.Column('contraseña', sa.VARCHAR(), nullable=True),
    sa.Column('tipo_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['tipo_id'], ['tipos_usuarios.id'], ),
    sa.PrimaryKeyConstraint('cedula')
    )
    op.create_index('ix_usuarios_nombres', 'usuarios', ['nombres'], unique=False)
    op.create_index('ix_usuarios_nacimiento', 'usuarios', ['nacimiento'], unique=False)
    op.create_index('ix_usuarios_direccion', 'usuarios', ['direccion'], unique=False)
    op.create_index('ix_usuarios_correo', 'usuarios', ['correo'], unique=False)
    op.create_index('ix_usuarios_contraseña', 'usuarios', ['contraseña'], unique=False)
    op.create_index('ix_usuarios_apellidos', 'usuarios', ['apellidos'], unique=False)
    op.create_table('productos',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('nombre', sa.VARCHAR(), nullable=True),
    sa.Column('descripcion', sa.VARCHAR(), nullable=True),
    sa.Column('altura_cm', sa.FLOAT(), nullable=True),
    sa.Column('anchura_cm', sa.FLOAT(), nullable=True),
    sa.Column('profundidad_cm', sa.FLOAT(), nullable=True),
    sa.Column('imagen', sa.BLOB(), nullable=True),
    sa.Column('peso_gramo', sa.FLOAT(), nullable=True),
    sa.Column('usuario_cedula', sa.VARCHAR(), nullable=True),
    sa.ForeignKeyConstraint(['usuario_cedula'], ['usuarios.cedula'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_productos_profundidad_cm', 'productos', ['profundidad_cm'], unique=False)
    op.create_index('ix_productos_peso_gramo', 'productos', ['peso_gramo'], unique=False)
    op.create_index('ix_productos_nombre', 'productos', ['nombre'], unique=False)
    op.create_index('ix_productos_imagen', 'productos', ['imagen'], unique=False)
    op.create_index('ix_productos_descripcion', 'productos', ['descripcion'], unique=False)
    op.create_index('ix_productos_anchura_cm', 'productos', ['anchura_cm'], unique=False)
    op.create_index('ix_productos_altura_cm', 'productos', ['altura_cm'], unique=False)
    # ### end Alembic commands ###
