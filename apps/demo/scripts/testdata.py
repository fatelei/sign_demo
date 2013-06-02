#!/usr/bin/env python
#-*-coding: utf8-*-

from demo.models.user import UserDAO
from demo.models.profile import ProfileDAO


class TestData(object):
    def insert_batch_user(self):
        for i in xrange(100):
            user_info = {"username": "test%d"%(i), "password": "123456"}
            profile_info = {"email": "test%d@test.com"%(i), "fullname": "testuser%d"%(i)}
            profile_id = ProfileDAO.insert_new_profile(profile_info)
            user_info["profile_id"] = profile_id
            user_info["role"] = 1
            user_id = UserDAO.insert_new_user(user_info)

    def insert_admin(self):
        user_info = {"username": "admin", "password": "123456"}
        profile_info = {"email": "test@test.com", "fullname": "admin"}
        profile_id = ProfileDAO.insert_new_profile(profile_info)
        user_info["profile_id"] = profile_id
        user_info["role"] = 2
        user_id = UserDAO.insert_new_user(user_info)


def run():
    testdata = TestData()
    testdata.insert_admin()
    testdata.insert_batch_user()

