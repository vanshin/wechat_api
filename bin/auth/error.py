#coding=utf8

'''error code'''

from . import auth
from altools.base.output import output
from altools.base.error import ParamExcp, UserExcp

@auth.errorhandler(ParamExcp)
def param_excp(e):
    return output(e.code, e.message)

@auth.errorhandler(UserExcp)
def user_excp(e):
    return output(e.code, e.message)
