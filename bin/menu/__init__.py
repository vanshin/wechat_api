#coding=utf-8

from flask import Blueprint

menu = Blueprint('menu', __name__)
from . import views, error
