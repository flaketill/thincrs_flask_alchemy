#!/usr/bin/env python3.7
# -*- coding: UTF-8 -*-
# -*- encoding: UTF-8 -*


from dotenv import load_dotenv
from app import create_app # pylint: disable=import-self


# Specificy a `.env` file containing key/value config values
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


app = create_app()

