#!/usr/bin/env python
#-*-coding: utf8-*-

import time

from datetime import datetime
from sqlalchemy import and_, select, func

from demo.models.tables import table
from demo.models.profile import ProfileDAO
from demo.utils.tools import encryption, check_password

from settings import ROLE_MAP

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
    def get_profile_id_by_user_id(cls, user_id):
        query = select([table.user.c.profile_id])\
                    .where(
                        and_(
                            table.user.c.id == int(user_id),
                            table.user.c.is_delete == 0))
        rst = table.execute(query).fetchone()
        if rst:
            return rst[0]
        else:
            return None


    @classmethod
    def remove_user_by_user_id(cls, user_id):
        update = table.user.update()\
                           .where(table.user.c.id == int(user_id))\
                           .values(is_delete = 1)
        table.execute(update)


    @classmethod
    def update_user_password(cls, user_id, password):
        password = encryption(password)
        update = table.user.update()\
                           .where(
                                and_(
                                    table.user.c.id == int(user_id),
                                    table.user.c.is_delete == 0))\
                           .values(password = password)
        table.execute(update)


    @classmethod
    def get_user_by_user_id(cls, user_id):
        query = table.user.select(table.user.c.id == int(user_id))
        query.append_whereclause(table.user.c.is_delete == 0)
        user = table.execute(query).first()
        return user


    @classmethod
    def check_user_exists(cls, username, password, role):
        query = table.user.select(table.user.c.username == username)
        query.append_whereclause(table.user.c.is_delete == 0)
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
                    .where(table.user.c.id == int(user_id))
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


    @classmethod
    def get_userlist_by_page(cls, page_num, ok_img, delete_img, offset = 20):
        data = []
        query_total = select([func.count(table.user.c.id)])
        total = table.execute(query_total).first()[0]
        query_user = table.user.select()
        query_user = query_user.limit(offset)
        query_user = query_user.offset(int(page_num - 1) * offset)
        user_list = table.execute(query_user).fetchall()

        for user in user_list:
            info = {}
            profile = ProfileDAO.get_user_profile_by_profile_id(user[8])
            info = {"user_id": user[0],
                    "username": user[1],
                    "fullname": profile.fullname,
                    "email": profile.email,
                    "phone": profile.phone,
                    "role": ROLE_MAP[user[3]],
                    "is_active": bool(user[4]),
                    "register_date": datetime.fromtimestamp(user[5]).strftime("%Y-%m-%d"),
                    "is_delete": bool(user[10])}
            if bool(user[4]):
                info["is_active"] = '<img src="{0}"/>'.format(ok_img)
            else:
                info["is_active"] = '<img src="{0}"/>'.format(delete_img)
            if bool(user[10]):
                info["is_delete"] = '<img src="{0}"/>'.format(ok_img)
            else:
                info["is_delete"] = '<img src="{0}"/>'.format(delete_img)
            data.append(info)
        per_page_data = {"total": total, "rows": data}
        return per_page_data

