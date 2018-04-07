#coding=utf-8

from flask import Blueprint

event = Blueprint('event', __name__)
from . import views, error
