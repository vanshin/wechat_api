#coding=utf-8

'''user'''

import os
import datetime
import config
import logging
import hashlib
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger()

from flask import request, current_app
from sqlalchemy.orm import sessionmaker

from altools.client import HttpClient
from altools.base.output import output
from altools.base.error import UserExcp

from . import menu

@menu.route('/weixin/menu', methods=['POST'])
def post_menu():
    pass
