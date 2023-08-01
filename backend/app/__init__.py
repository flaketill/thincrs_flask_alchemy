#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -*- encoding: UTF-8 -*


from flask import Flask
from flask.views import MethodView


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
    
    return app