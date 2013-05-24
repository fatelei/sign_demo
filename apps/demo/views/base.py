#!/usr/bin/env python
#-*-coding: utf8-*-

from tornado import web

from demo.models.user import UserDAO

class BaseHandler(web.RequestHandler):
    def get_login_url(self):
        return self.reverse_url("login")

    @property
    def user(self):
        return self.get_current_user()


    def get_current_user(self):
        user_id = self.get_secure_cookie("user_id")
        if user_id:
            user = UserDAO.get_user_by_user_id(user_id)
            if user:
                return user
            else:
                return None
        else:
            return None