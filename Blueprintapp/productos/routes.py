from flask import Blueprint, render_template

bp_productos = Blueprint(
    'productos',
    __name__,
    template_folder='templates'
)

@bp_productos.route('/')
def index():
    return render_template('producto/index.html')