#!/usr/bin/env python
#-*-coding: utf8-*-

import logging

from tornado import web

from demo.views.base import BaseHandler
from demo.utils.decorate import render, has_permission, log

from demo.models.user import UserDAO
from demo.models.profile import ProfileDAO

class LoginHandler(BaseHandler):
    @render(tpl = "login.html")
    def get(self):
        if self.user:
            self.redirect(self.reverse_url("index"))
        else:
            return {}

    @render()
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
            logging.warning(rst.keys)
            logging.warning(rst.id)
            self.set_secure_cookie("user_id", str(rst.id), expires_days = 1)
            return {"msg": u"登录成功"}


class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user_id")
        self.redirect(self.reverse_url("login"))


class AddUserHandler(BaseHandler):
    @render()
    @web.authenticated
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
        profile_info = {}
        profile_info["email"] = email
        profile_info["fullname"] = fullname
        profile_id = ProfileDAO.insert_new_profile(user_id, profile_info)
        user_info = {}
        user_info["username"] = username
        user_info["password"] = password
        user_info["profile_id"] = profile_id
        user_id = UserDAO.insert_new_user(user_info)
        return {"msg": u"添加用户成功"}

class UserProfileHandler(BaseHandler):
    @render("profile.html")
    @web.authenticated
    def get(self, user_id):
        data = {}
        try:
            profile_id = UserDAO.get_profile_id_by_user_id(user_id)
            if profile_id:
                profile = ProfileDAO.get_user_profile_by_user_id(profile_id)
                data["fullname"] = profile.fullname
                data["email"] = profile.email
                data["phone"] = profile.phone
                return data
            else:
                return {"errmsg": u"获取用户信息出错"}
        except:
            return {"errmsg": u"获取用户信息出错"}

    @render()
    @web.authenticated
    def post(self, user_id):
        fullname = self.get_argument("fullname", None)
        email = self.get_argument("email", None)
        phone = self.get_argument("phone", None)
        if not fullname and not email and not phone:
            return {"errmsg": u"修改用户个人信息出错"}
        else:
            values = {}
            if fullname:
                values["fullname"] = fullname
            if email:
                values["email"] = email
            if phone:
                values["phone"] = phone
            profile_id = UserDAO.get_profile_id_by_user_id(user_id)
            if profile_id:
                ProfileDAO.update_user_profile_by_user_id(profile_id, values)
                return {"msg": u"修改成功"}
            else:
                return {"errmsg": u"修改用户个人信息出错"}


class UserPwdHandler(BaseHandler):
    @render("pwdchange.html")
    @web.authenticated
    def get(self, user_id):
        return {}

    @render()
    @web.authenticated
    def post(self, user_id):
        password = self.get_argument("password", None)
        re_passsword = self.get_argument("re_password", None)
        if not password:
            return {"errmsg": u"请输入新密码"}
        if password != re_passsword:
            return {"errmsg": u"密码不一致"}
        UserDAO.update_user_password(user_id, password)
        return {"msg": u"修改密码成功"}



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


