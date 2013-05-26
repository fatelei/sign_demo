#!/usr/bin/env python
#-*-coding: utf8-*-

from tornado import web

from demo.views.base import BaseHandler
from demo.utils.decorate import render, has_permission, log

class IndexHandler(BaseHandler):
    @render("index.html")
    @web.authenticated
    def get(self):
        return {}

