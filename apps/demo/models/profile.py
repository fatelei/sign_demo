#!/usr/bin/env python
#-*-coding: utf8-*-

from sqlalchemy import select

from demo.models.tables import table


class ProfileDAO(object):
    @classmethod
    def insert_new_profile(cls, user_id, values):
        values["user_id"] = user_id
        ins = table.userprofile.insert().values(values)
        rst = table.execute(ins)
        _id = rst.inserted_primary_key[0]
        return _id