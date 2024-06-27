from sqlalchemy.orm import Session
from schemas import Respuesta
import categorias.models as models
import categorias.schemas as schemas
import productos.models as producto_models

def create_categoria(db: Session, categoria: schemas.CategoriaCrear):
    db_categoria = models.Categoria(nombre=categoria.nombre, descripcion=categoria.descripcion)
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)

    categoria = schemas.Categoria(nombre=db_categoria.nombre, descripcion=db_categoria.descripcion, id=db_categoria.id) 
    respuesta = Respuesta[schemas.Categoria](ok=True, mensaje='Categoría creada', data=categoria)
    return respuesta

def get_categoria(db: Session, categoria_id: int):
    returned = db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()

    if returned == None:
        return Respuesta[schemas.Categoria](ok=False, mensaje='Categoría no encontrada')

    categoria = schemas.Categoria(nombre=returned.nombre, descripcion=returned.descripcion, id=returned.id) 
    return Respuesta[schemas.Categoria](ok=True, mensaje='Categoría encontrada', data=categoria)

def get_categorias(db: Session):
    returned = db.query(models.Categoria).all()

    categorias = []

    for cat in returned:
        categoria = schemas.Categoria(nombre=cat.nombre, descripcion=cat.descripcion, id=cat.id) 
        categorias.append(categoria)

    respuesta = Respuesta[list[schemas.Categoria]](ok=True, mensaje='Categorías encontrada', data=categorias)
    return respuesta

def update_categoria(db: Session, categoria_id: int, categoria: schemas.CategoriaCrear):
    categoriaFound = db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()

    if categoriaFound == None:
        return Respuesta[schemas.Categoria](ok=False, mensaje='Categoría a actualiza no encontrada')
    
    categoriaFound.descripcion = categoria.descripcion
    categoriaFound.nombre = categoria.nombre
    db.commit()

    returned = db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()

    categoria = schemas.Categoria(nombre=returned.nombre, descripcion=returned.descripcion, id=returned.id) 
    respuesta = Respuesta[schemas.Categoria](ok=True, mensaje='Categorías actualizada', data=categoria)
    return respuesta

def delete_categoria(db: Session, categoria_id: int):
    categoriaFound = db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()

    if categoriaFound == None:
        return Respuesta[schemas.Categoria](ok=False, mensaje='Categoría a eliminar no encontrada')
    
    productos = db.query(producto_models.Producto).filter(producto_models.Producto.categoria_id == categoria_id).first()

    if productos:
        return Respuesta[schemas.Categoria](ok=False, mensaje='No se puede eliminar una categoría que esté siendo usada por un producto.')
    
    db.query(models.Categoria).filter(models.Categoria.id == categoria_id).delete()
    db.commit()
   
    return Respuesta[schemas.Categoria](ok=True, mensaje='Categoría eliminada')