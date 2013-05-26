#!/usr/bin/env python
#-*-coding: utf8-*-

from tornado.web import url

from demo.views.user.views import *
from demo.views.index import IndexHandler

handlers = [
	url("/", LoginHandler, name = "login"),
	url("/signcontact", IndexHandler, name = "index"),
	url("/userprofile/(\d+)", UserProfileHandler, name = "profile"),
	url("/userpwdchange/(\d+)", UserPwdHandler, name = "pwdchange")
]