#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -*- encoding: UTF-8 -*


from flask import Flask
from flask.views import MethodView
from .Users.resources import users_blueprint
from .Categories.resources import categories_blueprint
from .Config.settings import SQLALCHEMY_DATABASE_URI
from .Database import db


class HelloWorld(MethodView):
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
    app.register_blueprint(categories_blueprint)


    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    db.init_app(app)

    with app.app_context():
        db.create_all()
    
    return app