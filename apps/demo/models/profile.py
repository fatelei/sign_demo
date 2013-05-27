#!/usr/bin/env python
#-*-coding: utf8-*-

from sqlalchemy import select

from demo.models.tables import table


class ProfileDAO(object):
    @classmethod
    def insert_new_profile(cls, values):
        ins = table.userprofile.insert().values(values)
        rst = table.execute(ins)
        _id = rst.inserted_primary_key[0]
        return _id


    @classmethod
    def get_user_profile_by_profile_id(cls, profile_id):
        query = table.userprofile.select(table.userprofile.c.id == int(profile_id))
        profile = table.execute(query).first()
        return profile


    @classmethod
    def update_user_profile_by_profile_id(cls, profile_id, values):
        update = table.userprofile.update()\
                                  .where(table.userprofile.c.id == int(profile_id))\
                                  .values(values)
        table.execute(update)



