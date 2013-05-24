#!/usr/bin/env python
#-*-coding: utf8-*-

import time

from sqlalchemy import and_, select

from demo.models.tables import table
from demo.utils.tools import encryption, check_password

class UserDAO(object):
    @classmethod
    def insert_new_user(cls, values):
        values["password"] = encryption(values["password"])
        values["register_date"] = int(time.time())
        ins = table.user.insert().values(values)
        rst = table.execute(ins)
        _id = rst.inserted_primary_key[0]
        return _id


    @classmethod
    def get_user_by_user_id(cls, user_id):
        query = table.user.select(table.user.c.id == int(user_id))
        user = table.execute(query).first()
        return user


    @classmethod
    def check_user_exists(cls, username, password, role):
        query = table.user.select(table.user.c.username == username)
        rst = table.execute(query).first()
        if rst:
            pwd_check = check_password(rst.password, password)
            if pwd_check:
                if rst.role == int(role):
                    return rst
                else:
                    return False
            else:
                return False
        else:
            return False


    @classmethod
    def check_user_permission(cls, user_id, target):
        query = select([table.user.c.user_permission, talbe.user.c.role])\
                    where(table.user.c.id == int(user_id))
        rst = table.execute(query).first()
        if rst[0]:
            if rst[0]&target:
                return True
            else:
                return False
        elif rst[1] == 1:
            return True
        else:
            return False



