from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import random
import string

db = SQLAlchemy()
ma = Marshmallow()

random_str = string.ascii_letters + string.digits + string.ascii_uppercase
key = ''.join(random.choice(random_str) for i in range(12))

def secret_key(app):
    app.config['SECRET_KEY'] = key


def config_db(app):
    db.init_app(app)
    app.app_context().push()
    db.create_all(app=app)
    app.db = db


def config_ma(app):
    ma.init_app(app)


def config_bp(app):
    from ..routes import user_routes, address_routes, card_routes, cart_routes, category_routes, sub_category_routes, new_product_routes
    app.register_blueprint(user_routes.bp_users)
    app.register_blueprint(address_routes.bp_address)
    app.register_blueprint(card_routes.bp_card)
    app.register_blueprint(cart_routes.bp_cart)
    app.register_blueprint(category_routes.bp_category)
    app.register_blueprint(sub_category_routes.bp_sub_category)
    app.register_blueprint(new_product_routes.bp_product)


def config_photo():
    folder_storage = '.storage'
    picture_quality = 80
    photo = {'folder': folder_storage, 'quality': picture_quality}
    return photo