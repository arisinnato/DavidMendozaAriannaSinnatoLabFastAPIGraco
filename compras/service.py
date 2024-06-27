from sqlalchemy.orm import Session
from datetime import datetime
from schemas import Respuesta
import compras.models as models
import compras.schemas as schemas

<<<<<<< HEAD

=======
import productos.models as producto_models
>>>>>>> 3de6dc9 (Avances David)
import usuarios.service as usuario_service
import productos.service as producto_service
import tipo_compra.service as tipo_compra_service

def realizar_compra(db: Session, compra: schemas.CompraCrear):

    respuesta_usuario = usuario_service.buscar_usuario(db=db, cedula=compra.cliente_cedula)
    if not respuesta_usuario.ok:
<<<<<<< HEAD
        return Respuesta[schemas.Compra](ok=False, mensaje='No existe cliente registrado con la cédula con que intenta la compra')


    respuesta_producto = producto_service.get_producto(db=db, id=compra.producto_id)
    if not respuesta_producto.ok:
        return Respuesta[schemas.Compra](ok=False, mensaje='No existe producto registrado')


    respuesta_tipo_compra = tipo_compra_service.get_tipo_compra(db=db, id=compra.tipo_compra_id)
    if not respuesta_tipo_compra.ok:
        return Respuesta[schemas.Compra](ok=False, mensaje='No existe tipo de compra registrado')

   
=======
        return Respuesta[schemas.Compra](ok=False, mensaje='No existe cliente registrado con la cédula con que se intenta realizar la compra')

    respuesta_producto = producto_service.get_producto(db=db, id=compra.producto_id)
    if not respuesta_producto.ok:
        return Respuesta[schemas.Compra](ok=False, mensaje='No existe producto registrado del que se intenta realizar la compra')

    respuesta_tipo_compra = tipo_compra_service.get_tipo_compra(db=db, id=compra.tipo_compra_id)
    if not respuesta_tipo_compra.ok:
        return Respuesta[schemas.Compra](ok=False, mensaje='No existe tipo de compra registrado con el cual se intenta realizar la compra')

>>>>>>> 3de6dc9 (Avances David)

    db_compra = models.Compra(
        cantidad=compra.cantidad, 
        fecha=datetime.now, 
        cliente_cedula=compra.cliente_cedula, 
        producto_id=compra.producto_id, 
        tipo_compra_id=compra.tipo_compra_id, 
        estado_compra_id=1)
    db.add(db_compra)
    db.commit()
    db.refresh(db_compra)


    compra = schemas.Compra(id=db_compra.id, 
                            cantidad=db_compra.cantidad, 
                            cliente_cedula=db_compra.cliente_cedula, 
                            producto_id=db_compra.id, 
                            tipo_compra_id=db_compra.tipo_compra_id, 
                            estado_compra_id=db_compra.estado_compra_id) 
    respuesta = Respuesta[schemas.Compra](ok=True, mensaje='Compra realizada', data=compra)
    return respuesta


def aprobar_compra(db: Session, id_compra: int):

<<<<<<< HEAD

=======
>>>>>>> 3de6dc9 (Avances David)
    compra_found = db.query(models.Compra).filter(models.Compra.id == id_compra).first()

    if compra_found == None:
        return Respuesta[schemas.Compra](ok=False, mensaje='Compra a aprobar no encontrada')

<<<<<<< HEAD

=======
>>>>>>> 3de6dc9 (Avances David)
    compra_found.estado_compra_id = 2
    db.commit()

    return Respuesta[schemas.Compra](ok=True, mensaje='Compra aprobada exitosamente')


def rechazar_compra(db: Session, id_compra: int):

    compra_found = db.query(models.Compra).filter(models.Compra.id == id_compra).first()

    if compra_found == None:
        return Respuesta[schemas.Compra](ok=False, mensaje='Compra a rechazar no encontrada')

    compra_found.estado_compra_id = 3
    db.commit()

    return Respuesta[schemas.Compra](ok=True, mensaje='Compra rechazada exitosamente')

def listar_compras(db: Session): 
<<<<<<< HEAD
    return db.query(models.Compra).all()


=======
    returned = db.query(models.Compra).all()

    compras = []

    for com in returned:
        compra = schemas.Compra(id=returned.id, 
                            cantidad=returned.cantidad, 
                            cliente_cedula=returned.cliente_cedula, 
                            producto_id=returned.id, 
                            tipo_compra_id=returned.tipo_compra_id, 
                            estado_compra_id=returned.estado_compra_id) 
        compras.append(compra)

    respuesta = Respuesta[list[schemas.Compra]](ok=True, mensaje='Compras encontrada', data=compras)
    return respuesta
 
>>>>>>> 3de6dc9 (Avances David)
def get_compra(db: Session, id: int):
    returned = db.query(models.Compra).filter(models.Compra.id == id).first()

    if returned == None:
        return Respuesta[schemas.Compra](ok=False, mensaje='Compra no encontrada')

    compra = schemas.Compra(id=returned.id, 
                            cantidad=returned.cantidad, 
                            cliente_cedula=returned.cliente_cedula, 
                            producto_id=returned.id, 
                            tipo_compra_id=returned.tipo_compra_id, 
                            estado_compra_id=returned.estado_compra_id) 
    return Respuesta[schemas.Compra](ok=True, mensaje='Compra encontrada', data=compra)


def modificar_compra(db: Session, id: int, compra: schemas.CompraCrear): 
    lista = db.query(models.Compra).all()
    for este in lista: 
        if este.id == id: 
            este.cantidad = compra.cantidad
            este.fecha = compra.fecha
            este.cliente_cedula = compra.cliente_cedula
            este.producto_id = compra.producto_id
            este.tipo_compra_id = compra.tipo_compra_id
            este.estado_compra_id = compra.estado_compra_id
            break
    db.commit()
    return este

def eliminar_compra(db: Session, id: int): 
    compra = db.query(models.Compra).filter(models.Compra.id == id).first()
    db.delete(compra)
    db.commit()
<<<<<<< HEAD
    return compra
=======
    return compra

def listar_compras_para_artesano(db: Session, cedula: int): 
    returned = db.query(models.Compra, producto_models.Producto).\
        join(producto_models.Producto, models.Compra.producto_id == producto_models.Producto.id).\
        filter(producto_models.Producto.usuario_cedula == cedula).all()
    
    compras = []

    for com in returned:
        compra = schemas.Compra(id=returned.id, 
                            cantidad=returned.cantidad, 
                            cliente_cedula=returned.cliente_cedula, 
                            producto_id=returned.id, 
                            tipo_compra_id=returned.tipo_compra_id, 
                            estado_compra_id=returned.estado_compra_id) 
        compras.append(compra)

    respuesta = Respuesta[list[schemas.Compra]](ok=True, mensaje='Lista de las compras realizadas al artesano encontrada', data=compras)
    return respuesta
>>>>>>> 3de6dc9 (Avances David)
