from flask import Blueprint, render_template

bp_clientes = Blueprint(
    'clientes',
    __name__,
    template_folder='templates'
)

@bp_clientes.route('/')
def index():
    return render_template('cliente/index.html')