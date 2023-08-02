#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -*- encoding: UTF-8 -*


from flask.views import MethodView
from flask import Blueprint, request, jsonify
import logging


# Configure the logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
categories_blueprint = Blueprint("Categories_blueprint", __name__, url_prefix="/api/")


categories = [
    {'id': 1, 'name': 'Category 1'},
    {'id': 2, 'name': 'Category 2'},
    {'id': 3, 'name': 'Category 3'},
    {'id': 10, 'name': 'Category 10'},
    {'id': 100, 'name': 'Category 100'},
]


class Categories(MethodView):
    def get(self):
        return [{ 'name': 'armando'},
                 {'name': 'test'}]


class CategoriesList(MethodView):
    def get(self):
        """Get all Categories
        """
        return jsonify(categories)


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