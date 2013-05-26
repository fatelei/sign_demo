#!/usr/bin/env python
#-*-coding: utf8-*-

import json
import logging

from tornado.web import HTTPError

from demo.models.user import UserDAO
from demo.models.log import LogDAO
from demo.utils.tools import get_target_module


def render(tpl = None):
    def real_decorater(func):
        def wraper(self, *args, **kwargs):
            rst = func(self, *args, **kwargs)
            if tpl:
                return self.render(tpl, data = rst)
            else:
                self.write(json.dumps(rst))
        return wraper
    return real_decorater


def has_permission(model, op):
    def real_decorater(func):
        def wraper(self, *args, **kwargs):
            user = self.user
            if not user:
                raise HTTPError(403)
            else:
                target = get_target_module(modal, op)
                rst = UserDAO.check_user_permission(user.id, target)
                if not rst:
                    raise HTTPError(403)
                else:
                    return func(self, *args, **kwargs)
        return wraper
    return real_decorater


def log(op_target):
    def real_decorater(func):
        def wraper(self, *args, **kwargs):
            user = self.user
            if not user:
                raise HTTPError(403)
            else:
                values = {}
                values["op_user"] = user.username
                values["op_target"] = op_target
                LogDAO.insert_new_log(values)
                return func(self, *args, **kwargs)
        return wraper
    return real_decorater



