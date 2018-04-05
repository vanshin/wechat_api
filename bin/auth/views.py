#coding=utf8

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

from . import auth

@auth.route('/wechat/auth/token', methods=['POST', 'GET'])
def post_event():

    d = request.values


    signature = d.get('signature')
    timestamp = d.get('timestamp')
    nonce = d.get('nonce')
    echostr = d.get('echostr')

    log.debug('signature={}, timestamp={}, nonce={}, echostr={}'.format(signature, timestamp, nonce, echostr))

    token = 'weixin_e311ec83943f'
    sha1 = hashlib.sha1()
    si_list = [token, timestamp, nonce]
    si_list.sort()
    for i in si_list:
        i = i.encode('utf8')
        sha1.update(i)
    hashcode = sha1.hexdigest()
    log.debug('signature={}, hashcode={}'.format(signature, hashcode))
    if hashcode == signature:
        return echostr
    else:
        return ''
