#!/usr/bin/env python
#-*-coding: utf8-*-

from tornado import web

from demo.views.base import BaseHandler
from demo.utils.decorate import render, has_permission, log

from demo.models.user import UserDAO
from demo.models.profile import ProfileDAO

class LoginHandler(BaseHandler):
	@render(tpl = "login.html")
	def get(self):
		if self.user:
			raise web.HTTPError(403)
		else:
			return {}


	@render(tpl = "login.html")
	def post(self):
		username = self.get_argument("username", None)
		password = self.get_argument("password", None)
		role = self.get_argument("role", None)
		if not username:
			return {"errmsg": u"请输入用户名"}
		if not password:
			return {"errmsg": u"请输入密码"}
		rst = UserDAO.check_user_exists(username, password, role)
		if not rst:
			return {"errmsg": u"用户名或密码错误"}
		else:
			self.set_secure_cookie(rst.id)
			self.write("ok")


class LogoutHandler(BaseHandler):
	def get(self):
		self.clear_cookie("user_id")
		self.redirect(self.reverse_url("login"))


class RegisterHandler(BaseHandler):
	@render(tpl = "register.html")
	def get(self):
		if self.user:
			raise HTTPError(403)
		else:
			return {}

	@render(tpl = "register.html")
	def post(self):
		username = self.get_argument("username", None)
		password = self.get_argument("password", None)
		email = self.get_argument("email", None)
		fullname = self.get_argument("fullname", None)
		if not username:
			return {"errmsg": u"请填写用户名"}
		if not password:
			return {"errmsg": u"请填写密码"}
		if not email:
			return {"errmsg": u"请填写邮箱"}
		if not fullname:
			return {"errmsg": u"请填写真实姓名"}
		user_info = {}
		user_info["username"] = username
		user_info["password"] = password
		user_id = UserDAO.insert_new_user(user_info)
		profile_info = {}
		profile_info["email"] = email
		profile_info["fullname"] = fullname
		ProfileDAO.insert_new_profile(user_id, profile_info)
		self.redirect(self.reverse_url("login"))


class UserProfileHandler(BaseHandler):
	@render()
	@web.authenticated
	def get(self, user_id):
		pass

	@render()
	@web.authenticated
	def post(self, user_id):
		pass


class UserRemoveHandler(BaseHandler):
	@render()
	@web.authenticated
	def post(self, user_id):
		pass


class UserListHandelr(BaseHandler):
	@render()
	@web.authenticated
	def get(self, page = 1):
		pass


