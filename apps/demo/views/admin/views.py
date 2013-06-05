#!/usr/bin/env python
#-*-coding: utf8-*-

from tornado import web

from demo.models.log import LogDAO
from demo.utils.decorate import render
from demo.views.base import BaseHandler

class LogListHandler(BaseHandler):
    @render("log.html")
    @web.authenticated
    def get(self):
        return {}


class LogAjaxListHandler(BaseHandler):
    def check_xsrf_cookie(self):
        pass

    @render()
    @web.authenticated
    def post(self):
        page = int(self.get_argument("page", 1))
        offset = int(self.get_argument("row", 20))
        data = LogDAO.get_log_list(page, offset)
        return data
