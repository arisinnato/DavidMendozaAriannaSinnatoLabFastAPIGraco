from sqlalchemy.orm import Session
from schemas import Respuesta
import categorias.models as models
import categorias.schemas as schemas
import productos.models as producto_models

def crear__una_categoria(db: Session, categoria: schemas.Categoria_a_Crear):
    db_categoria = models.Categoria(nombre=categoria.nombre, descripcion=categoria.descripcion)
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)

    categoria = schemas.Categoria(nombre=db_categoria.nombre, descripcion=db_categoria.descripcion, id=db_categoria.id) 
    respuesta = Respuesta[schemas.Categoria](ok=True, mensaje='la Categoría ha sido creada', data=categoria)
    return respuesta

def get_categoria(db: Session, categoria_id: int):
    returned = db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()

    if returned == None:
        return Respuesta[schemas.Categoria](ok=False, mensaje='la Categoría no se ha encontrado')

    categoria = schemas.Categoria(nombre=returned.nombre, descripcion=returned.descripcion, id=returned.id) 
    return Respuesta[schemas.Categoria](ok=True, mensaje='la Categoría se ha  encontrado', data=categoria)

"""def get_categorias(db: Session):
    returned = db.query(models.Categoria).all()

    categorias = []

    for cat in returned:
        categoria = schemas.Categoria(nombre=cat.nombre, descripcion=cat.descripcion, id=cat.id) 
        categorias.append(categoria)

    respuesta = Respuesta[list[schemas.Categoria]](ok=True, mensaje='Categorías encontrada', data=categorias)
    return respuesta

def actualizar_una_categoria(db: Session, categoria_id: int, categoria: schemas.Categoria_a_Crear):
    categoriaFound = db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()

    if categoriaFound == None:
        return Respuesta[schemas.Categoria](ok=False, mensaje='Categoría que dea actualizar no se a  encontrado')
    
    categoriaFound.descripcion = categoria.descripcion
    categoriaFound.nombre = categoria.nombre
    db.commit()

    returned = db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()

    categoria = schemas.Categoria(nombre=returned.nombre, descripcion=returned.descripcion, id=returned.id) 
    respuesta = Respuesta[schemas.Categoria](ok=True, mensaje='Categorías actualizada', data=categoria)
    return respuesta"""

def eliminar_una_categoria(db: Session, categoria_id: int):
    categoriaFound = db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()

    if categoriaFound == None:
        return Respuesta[schemas.Categoria](ok=False, mensaje='la categoría que desea eliminar no se haa encontrado')
    
    productos = db.query(producto_models.Producto).filter(producto_models.Producto.categoria_id == categoria_id).first()

    if productos:
        return Respuesta[schemas.Categoria](ok=False, mensaje='No puede eliminar una categoría que esta siendo  usada por un producto')
    
    db.query(models.Categoria).filter(models.Categoria.id == categoria_id).delete()
    db.commit()
   
    return Respuesta[schemas.Categoria](ok=True, mensaje='ñas Categoría se ha eliminado')













def get_categorias(db: Session):
    returned = db.query(models.Categoria).all()

    categorias = []

    for cat in returned:
        categoria = schemas.Categoria(nombre=cat.nombre, descripcion=cat.descripcion, id=cat.id) 
        categorias.append(categoria)

    respuesta = Respuesta[list[schemas.Categoria]](ok=True, mensaje='las Categorías se han encontrado encontrada', data=categorias)
    return respuesta

def actualizar_una_categoria(db: Session, categoria_id: int, categoria: schemas.Categoria_a_Crear):
    categoriaFound = db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()

    if categoriaFound == None:
        return Respuesta[schemas.Categoria](ok=False, mensaje='las Categoría que quiere actualizar no se haa  encontrado')
    
    categoriaFound.descripcion = categoria.descripcion
    categoriaFound.nombre = categoria.nombre
    db.commit()

    returned = db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()

    categoria = schemas.Categoria(nombre=returned.nombre, descripcion=returned.descripcion, id=returned.id) 
    respuesta = Respuesta[schemas.Categoria](ok=True, mensaje='ña Categoría se ha actualizado', data=categoria)
    return respuesta