#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -*- encoding: UTF-8 -*


from flask.views import MethodView
from flask import Blueprint, request


from app.Roles.models import Roles


roles_blueprint = Blueprint("roles_blueprint", __name__, url_prefix="/api/")


class RolesList(MethodView):
    def get(self):
        return [{ 'name': 'admin'},
                 {'name': 'user'}]


roles_blueprint.add_url_rule(
                            "roles",
                            view_func=UsersList.as_view("roles_list")
)

