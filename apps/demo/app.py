#!/usr/bin/env python
#-*-coding: utf8-*-

import os
import tornado.ioloop

from tornado import web
from tornado.options import options

from urls import handlers

BASE_DIR = os.path.realpath(os.path.dirname(__file__))


SERVER_SETTINGS = {
	"debug": True,
	"cookie_secret": "dasdasd9uasdawhyq028713ui2urqwrejhwqoifusdifw",
	"xsrf_cookies": True,
	"template_path": "{0}/{1}".format(BASE_DIR, "templates"),
	"static_path": "{0}/{1}".format(BASE_DIR, "static")
}


def run():
	app = web.Application(handlers, **SERVER_SETTINGS)
	app.listen(options.sign_server_port)
	tornado.ioloop.IOLoop.instance().start()
	

if __name__ == "__main__":
	run()

