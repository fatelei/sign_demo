#!/usr/bin/env python
#-*-coding: utf8-*-

from tornado.web import url

from demo.views.user.views import *
from demo.views.contract_template.views import *
from demo.views.admin.views import *
from demo.views.index import IndexHandler

handlers = [
	url("/", LoginHandler, name = "login"),
	url("/logout", LogoutHandler, name = "logout"),
	url("/signcontact", IndexHandler, name = "index"),
	url("/userprofile/(\d+)", UserProfileHandler, name = "profile"),
	url("/userpwdchange/(\d+)", UserPwdHandler, name = "pwdchange"),
	url("/userlist", UserListHandler, name = "userlist"),
	url("/userlistajax", UserListAjaxHandler, name = "userlist_ajax"),
	url("/userremove", UserRemoveHandler, name = "userremove"),
	url("/useradd", UserAddHandler, name = "useradd"),
	url("/ctlist", CTListHandler, name = "ctlist"),
	url("/ctlistajax", CTAjaxListHandler, name = "ctlist_ajax"),
	url("/ctadd", CTAddHandler, name = "ctadd"),
	url("/ctupdate/(\d+)", CTUpdateHandler, name = "ctupdate"),
	url("/ctremove", CTRemoveHandler, name = "ctremove"),
	url("/loglist", LogListHandler, name = "loglist"),
	url("/logajaxlist", LogAjaxListHandler, name = "logajaxlist"),
	url("/csign/(\d+)", CTSignHandler, name = "csign")
]