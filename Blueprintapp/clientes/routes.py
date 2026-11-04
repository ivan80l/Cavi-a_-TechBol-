from flask import Blueprint, render_template, request, redirect, url_for
from Blueprintapp.app import db
from Blueprintapp.clientes.models import Cliente

bp_clientes = Blueprint('clientes', __name__, template_folder='templates')

@bp_clientes.route('/')
def index():
    clientes = Cliente.query.all()
    return render_template('cliente/index.html', clientes=clientes)

@bp_clientes.route('/crear', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        cliente = Cliente(
            nombre=request.form['nombre'],
            telefono=request.form['telefono']
        )
        db.session.add(cliente)
        db.session.commit()
        return redirect(url_for('clientes.index'))

    return render_template('cliente/create.html')

@bp_clientes.route('/editar/<int:id>', methods=['GET', 'POST'])
def edit(id):
    cliente = Cliente.query.get_or_404(id)

    if request.method == 'POST':
        cliente.nombre = request.form['nombre']
        cliente.telefono = request.form['telefono']
        db.session.commit()
        return redirect(url_for('clientes.index'))

    return render_template('cliente/edit.html', cliente=cliente)

@bp_clientes.route('/eliminar/<int:id>', methods=['POST'])
def delete(id):
    cliente = Cliente.query.get_or_404(id)

    if cliente.pedidos:
        return 'No se puede eliminar porque tiene pedidos asociados.'

    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('clientes.index'))