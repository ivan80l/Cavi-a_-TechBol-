#pedidos
from Blueprintapp.app import db

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    monto = db.Column(db.Float, nullable=False)

    producto_id = db.Column(
        db.Integer,
        db.ForeignKey('producto.id'),
        nullable=False
    )

    cliente_id = db.Column(
        db.Integer,
        db.ForeignKey('cliente.id'),
        nullable=False
    )

    producto = db.relationship('Producto', back_populates='pedidos')
    cliente = db.relationship('Cliente', back_populates='pedidos')