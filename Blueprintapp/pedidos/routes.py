from flask import Blueprint, render_template

bp_pedidos = Blueprint(
    'pedidos',
    __name__,
    template_folder='templates'
)

@bp_pedidos.route('/')
def index():
    return render_template('pedido/index.html')