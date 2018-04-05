#coding=utf8

'''error code'''

from . import menu
from altools.base.output import output
from altools.base.error import ParamExcp, UserExcp

@menu.errorhandler(ParamExcp)
def param_excp(e):
    return output(e.code, e.message)

@menu.errorhandler(UserExcp)
def user_excp(e):
    return output(e.code, e.message)
