#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -*- encoding: UTF-8 -*


from flask.views import MethodView
from flask import Blueprint, request


categories_blueprint = Blueprint("Categories_blueprint", __name__, url_prefix="/api/")


class Categories(MethodView):
    def get(self):
        return [{ 'name': 'armando'},
                 {'name': 'test'}]


class CategoriesList(MethodView):
    def get(self):
        return [{ 'name': 'armando'},
                 {'name': 'test'}]


class CategoriesID(MethodView):
    def get(self):
        pass


categories_blueprint.add_url_rule(
    "categories",
    view_func=CategoriesList.as_view("Categories_list")
)

categories_blueprint.add_url_rule(
                            "categories",
                            view_func=Categories.as_view("categories")
)

categories_blueprint.add_url_rule(
                            "/categories/<category_id>",
                            view_func=CategoriesID.as_view("categories_id")
)