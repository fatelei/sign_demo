#!/usr/bin/env python
#-*-coding: utf8-*-

from demo.models.user import UserDAO
from demo.models.profile import ProfileDAO

def insert_user():
    user_info = {"username": "admin", "password": "123456"}
    profile_info = {"email": "test@test.com", "fullname": "admin"}
    profile_id = ProfileDAO.insert_new_profile(profile_info)
    user_info["profile_id"] = profile_id
    user_info["role"] = 2
    user_id = UserDAO.insert_new_user(user_info)
