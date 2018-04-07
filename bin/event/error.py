#coding=utf8

'''error code'''

from . import event
from altools.base.output import output
from altools.base.error import ParamExcp, UserExcp

@event.errorhandler(ParamExcp)
def param_excp(e):
    return output(e.code, e.message)

@event.errorhandler(UserExcp)
def user_excp(e):
    return output(e.code, e.message)
