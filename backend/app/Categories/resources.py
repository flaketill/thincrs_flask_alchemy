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

class CategoriesHandle(object):
    """Class that handles categories."""
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg


    def get_category_by_id(category_id):
        return next((category for category in categories if category['id'] == category_id), None)

    
    def create_category(new_category):
        categories.append(new_category)
        return new_category['id']
        


class Categories(MethodView):
    def get(self,category_id):
        category = CategoriesHandle.get_category_by_id(category_id)

        if category:
            return jsonify(category)

        return jsonify({'error': 'Category not found'}), 404


    def delete(self, category_id):
        # Find index of item with id 3
        index_to_remove = next(i for i, item in enumerate(categories) if item['id'] == category_id)

        # Remove item at index
        del categories[index_to_remove]

        logging.debug(f"{categories}")

        return jsonify({})


class CategoriesList(MethodView):
    def get(self):
        """Get all Categories
        """
        return jsonify(categories)


class CategoriesItem(MethodView):
    def post(self):
        new_category = request.json

        logging.debug(f'{new_category}')

        if new_category.get('id') is None:
            logging.debug(f"{'message': 'Error: missing category id'}")
            return jsonify({'error': 'Missing category id'}), 400

        if new_category.get('name') is None:
            logging.debug(f"{'message': 'Error: missing category name'}")
            return jsonify({'error': 'Missing category name'}), 400            

        new_category_id = CategoriesHandle.create_category(new_category)
        return jsonify({'category_id': new_category_id}), 201


categories_blueprint.add_url_rule(
    "categories",
    view_func=CategoriesList.as_view("Categories_list")
)

categories_blueprint.add_url_rule(
                            "categories",
                            view_func=CategoriesItem.as_view("category_id")
)

categories_blueprint.add_url_rule(
                            "/categories/<int:category_id>",
                            view_func=Categories.as_view("categories")
)
