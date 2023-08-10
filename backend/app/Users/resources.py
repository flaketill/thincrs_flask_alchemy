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


    def patch(self, user_id):
        if not request.json:
            return { 'error': {'message': 'The payload is not valid JSON', "status":"failure"}}, 400
        

        if user_id is None:
            return { 'message': 'You have not entered the user id correctly'}, 400


        user = Users.get_by_id(user_id)


        if user:
            data = request.get_json()

            first_name = data.get('first_name')
            last_name = data.get('last_name')
            email = data.get('email')
            role_id = data.get('role_id')

            
            if first_name is not None:
                user.first_name =  first_name

            if last_name is not None:
                user.last_name = last_name

            if email is not None:
                user.email = email
            
            if role_id is not None:
                user.rol_id = int(role_id)

            user.update()

            if user:
                json_data = user.to_json()
                return jsonify(json_data), 201


        return { 'message': 'error'}, 400


class UsersList(MethodView):
    def get(self):
        """Return all users, ordered by date.
        """        
        users = Users.return_all()
        logging.debug(f'{users}')
        return jsonify(users), 200


class UsersResources(MethodView):
    def post(self):

        if not request.json:
            return { 'message': 'You have not entered payload correctly'}, 400

        data = request.get_json()

        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        role_id = int(data.get('role_id'))

        if first_name is None:
            return { 'message': 'You have not entered your first_name correctly'}, 400

        if email is None:
            return { 'message': 'You have not entered your email address correctly'}, 400

        if role_id is None:
            return { 'message': 'You have not entered the role id correctly'}, 400


        user = Users(first_name=first_name, last_name=last_name, email=email, rol_id=role_id)
        user.save()

        
        if user:
            json_data = user.to_json()
            return jsonify(json_data), 200

        return { 'message': 'error'}, 400


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
