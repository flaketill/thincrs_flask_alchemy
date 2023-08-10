#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -*- encoding: UTF-8 -*


from flask.views import MethodView
from flask import Blueprint, request, jsonify
from app.Users.models import Users
import logging
import json


# Configure the logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
users_blueprint = Blueprint("users_blueprint", __name__, url_prefix="/api/")


class UsersItem(MethodView):
    def get(self,user_id):

        logging.debug(f'{user_id}')
        user = Users.get_by_id(user_id)

        if user:            
            json_data = user.to_json()
            return jsonify(json_data), 200

        return jsonify({'error': 'User not found'}), 404


class UsersList(MethodView):
    def get(self):
        """Return all users, ordered by date.
        """        
        users = Users.return_all()
        logging.debug(f'{users}')
        return jsonify(users), 200


class UsersResources(MethodView):
    def post(self):
        data = request.get_json()

        email = data.get('email')
        username = data.get('username')

        if email is None:
            return { 'message': 'You have not entered your email address correctly'}, 400

        if username is None:
            return { 'message': 'You have not entered your username correctly'}, 400


        return { 'message': 'Bienvenido! :D'}


users_blueprint.add_url_rule(
                            "users",
                            view_func=UsersList.as_view("users_list")
)


users_blueprint.add_url_rule(
                            "users",
                            view_func=UsersResources.as_view("users")
)


users_blueprint.add_url_rule(
                            "users/<int:user_id>",
                            view_func=UsersItem.as_view("user")
)


