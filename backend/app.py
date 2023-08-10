#!/usr/bin/env python3.7
# -*- coding: UTF-8 -*-
# -*- encoding: UTF-8 -*


from dotenv import load_dotenv
from app import create_app # pylint: disable=import-self


load_dotenv('.env') #the path to your .env file (or any other file of environment variables you want to load)
app = create_app()
