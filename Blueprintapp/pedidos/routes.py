from datetime import date
from flask import Blueprint, render_template, request, redirect, url_for
from Blueprintapp.app import db
from Blueprintapp.pedidos.models import Pedido
from Blueprintapp.clientes.models import Cliente
from Blueprintapp.productos.models import Producto

bp_pedidos = Blueprint('pedidos', __name__, template_folder='templates')

@bp_pedidos.route('/')
def index():
    pedidos = Pedido.query.all()
    return render_template('pedido/index.html', pedidos=pedidos)

@bp_pedidos.route('/crear', methods=['GET', 'POST'])
def create():
    clientes = Cliente.query.all()
    productos = Producto.query.all()

    if request.method == 'POST':
        pedido = Pedido(
            fecha=date.fromisoformat(request.form['fecha']),
            monto=float(request.form['monto']),
            cliente_id=int(request.form['cliente_id']),
            producto_id=int(request.form['producto_id'])
        )
        db.session.add(pedido)
        db.session.commit()
        return redirect(url_for('pedidos.index'))

    return render_template(
        'pedido/create.html',
        clientes=clientes,
        productos=productos
    )

@bp_pedidos.route('/editar/<int:id>', methods=['GET', 'POST'])
def edit(id):
    pedido = Pedido.query.get_or_404(id)
    clientes = Cliente.query.all()
    productos = Producto.query.all()

    if request.method == 'POST':
        pedido.fecha = date.fromisoformat(request.form['fecha'])
        pedido.monto = float(request.form['monto'])
        pedido.cliente_id = int(request.form['cliente_id'])
        pedido.producto_id = int(request.form['producto_id'])

        db.session.commit()
        return redirect(url_for('pedidos.index'))

    return render_template(
        'pedido/edit.html',
        pedido=pedido,
        clientes=clientes,
        productos=productos
    )

@bp_pedidos.route('/eliminar/<int:id>', methods=['POST'])
def delete(id):
    pedido = Pedido.query.get_or_404(id)
    db.session.delete(pedido)
    db.session.commit()
    return redirect(url_for('pedidos.index'))