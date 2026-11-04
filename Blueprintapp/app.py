from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app():

    app = Flask(__name__, template_folder='templates')

    app.config['SECRET_KEY'] = 'clave_secreta_desarrollo'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bd_techbol.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar Blueprints
    from Blueprintapp.clientes.routes import bp_clientes
    from Blueprintapp.productos.routes import bp_productos
    from Blueprintapp.pedidos.routes import bp_pedidos
    from Blueprintapp.core.routes import bp_core

    app.register_blueprint(bp_clientes, url_prefix='/clientes')
    app.register_blueprint(bp_productos, url_prefix='/productos')
    app.register_blueprint(bp_pedidos, url_prefix='/pedidos')
    app.register_blueprint(bp_core, url_prefix='/')

    from Blueprintapp.clientes.models import Cliente
    from Blueprintapp.productos.models import Producto
    from Blueprintapp.pedidos.models import Pedido

    return app