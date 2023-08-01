#!/usr/bin/env python3.7
# -*- coding: UTF-8 -*-
# -*- encoding: UTF-8 -*


import sys
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'