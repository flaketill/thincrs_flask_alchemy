#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -*- encoding: UTF-8 -*


from flask import Flask
from flask.views import MethodView
from .Users.resources import users_blueprint
from .Categories.resources import categories_blueprint
from settings import SQLALCHEMY_DATABASE_URI
from .Database import db
from .Categories.models import Category
from app.Roles.resources import roles_blueprint


from flask_migrate import Migrate
from os import environ, path


migrate = Migrate()
basedir = path.abspath(path.dirname(__file__))


class HelloWorld(MethodView):
    """ Hello world class example with Methods: POST, GET, PUT/PATCH, DELETE

        C -> Create -> POST
        R -> Read -> GET
        U -> Update -> PUT / PATCH
        D -> Delete -> DELETE
    """
    def get(self):
    	return { 'message': 'Hey there! Hello World :)'}

    def post(self):
    	return None

    def patch(self):
    	# exits and update
        return None

    def delete(self):
        #
    	return None


def create_app():
    app = Flask(__name__)
    
    
    hello_word = HelloWorld.as_view("hello_word")
    

    app.add_url_rule('/', view_func=hello_word)
    
    
    app.register_blueprint(users_blueprint)
    app.register_blueprint(roles_blueprint)
    app.register_blueprint(categories_blueprint)


    # Configuring Flask From Class Objects
    # Specificy a `../settings.py` file containing project settings
    app.config.from_pyfile(path.join(basedir, '../settings.py'))
    db.init_app(app)

    with app.app_context():
        migrate.init_app(app, db)


    return app

    