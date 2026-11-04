from flask import Blueprint, render_template, request, redirect, url_for
from Blueprintapp.app import db
from Blueprintapp.productos.models import Producto

bp_productos = Blueprint('productos', __name__, template_folder='templates')

@bp_productos.route('/')
def index():
    productos = Producto.query.all()
    return render_template('producto/index.html', productos=productos)

@bp_productos.route('/crear', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        producto = Producto(
            nombre=request.form['nombre'],
            precio=float(request.form['precio']),
            stock=int(request.form['stock'])
        )
        db.session.add(producto)
        db.session.commit()
        return redirect(url_for('productos.index'))

    return render_template('producto/create.html')

@bp_productos.route('/editar/<int:id>', methods=['GET', 'POST'])
def edit(id):
    producto = Producto.query.get_or_404(id)

    if request.method == 'POST':
        producto.nombre = request.form['nombre']
        producto.precio = float(request.form['precio'])
        producto.stock = int(request.form['stock'])
        db.session.commit()
        return redirect(url_for('productos.index'))

    return render_template('producto/edit.html', producto=producto)

@bp_productos.route('/eliminar/<int:id>', methods=['POST'])
def delete(id):
    producto = Producto.query.get_or_404(id)

    if producto.pedidos:
        return 'No se puede eliminar porque tiene pedidos asociados.'

    db.session.delete(producto)
    db.session.commit()
    return redirect(url_for('productos.index'))