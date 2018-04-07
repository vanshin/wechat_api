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
from altools.base.deco import show_args

from .base import WeChatDef
from . import event

@event.route('/wechat/event', methods=['POST', 'GET'])
def post_event():


    @show_args
    def auth(d):
        '''认证'''
        args = {}
        auth_args_key = ['signature', 'timestamp', 'nonce', 'echostr']
        for arg in auth_args_key:
            tmp_value = d.get(arg)
            if not tmp_value:
                log.info('args {} is {}'.format(arg, tmp_value))
                raise ParamExcp('微信验证参数缺少')
            args[arg] = tmp_value

        signature = args['signature']
        timestamp = args['timestamp']
        nonce = args['nonce']
        echostr = args['echostr']

        sha1 = hashlib.sha1()
        si_list = [WeChatDef.WEIXIN_TOKEN, timestamp, nonce]
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

    def event(d):
        pass

    d = request.values

    mode = 'event'
    if 'signature' in d:
        mode = 'auth'

    wechat_handler = {
        'auth': auth,
        'event': event
    }

    handler = wechat_handler.get(mode)

    if not handler:
        raise ParamExcp('missing of handler for {}'.format(mode))
    ret = handler(d)
    return ret
