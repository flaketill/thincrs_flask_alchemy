#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -*- encoding: UTF-8 -*


from flask.views import MethodView
from flask import Blueprint, request, jsonify
import logging
from .models import Category


# Configure the logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# Operations on categories
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
    def __init__(self, model):
        self.model = model

    
    def get(self,category_id):
        category = CategoriesHandle.get_category_by_id(category_id)

        if category:
            return jsonify(category)

        return jsonify({'error': 'Category not found'}), 404


    def delete(self, category_id):
        # Find index of item with category id
        index_to_remove = next(i for i, item in enumerate(categories) if item['id'] == category_id)

        # Remove item at index
        del categories[index_to_remove]

        logging.debug(f"{categories}")

        return jsonify({}), 204


class CategoriesList(MethodView):
    def __init__(self, model):
        self.model = model        

    def get(self):
        """Get all Categories
        """
        return jsonify(categories)


class CategoriesItem(MethodView):
    def __init__(self, model):
        self.model = model    
    

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


def register_api(app, model, name):
    category_list = CategoriesList.as_view(f"{name}_list", model)    
    category = Categories.as_view(f"{name}", model)
    category_item = CategoriesItem.as_view(f"{name}_item", model)

    
    app.add_url_rule(f"/{name}", view_func=category_list)
    app.add_url_rule(f"/{name}/", view_func=category_list)
    app.add_url_rule(f"/{name}/<int:category_id>", view_func=category)    
    app.add_url_rule(f"/{name}", view_func=category_item)
    app.add_url_rule(f"/{name}/", view_func=category_item)


register_api(categories_blueprint, Category, "categories")

