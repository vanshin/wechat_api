#coding=utf8

import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger()

from altools.base.deco import show_args
from altools.base.error import ParamExcp, UserExcp

class WeChatDef(object):

    WEIXIN_TOKEN = 'weixin_e311ec83943f'
