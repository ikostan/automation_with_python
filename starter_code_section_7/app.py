import os

from flask import Flask
from flask_restful import Api

from starter_code_section_7.resources.item import Item, ItemList
from starter_code_section_7.resources.store import Store, StoreList
from starter_code_section_7.resources.user import UserRegistration

app = Flask(__name__)

app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegistration, '/register')


if __name__ == '__main__':
    from starter_code_section_6.db import db

    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)
