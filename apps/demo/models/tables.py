#!/usr/bin/env python
#-*-coding: utf8-*-

from sqlalchemy import exc
from sqlalchemy import create_engine, MetaData

from settings import DATABASE

class Tables(object):
    meta = MetaData()

    def __init__(self):
        self.e = create_engine(DATABASE["conn"],
                               encoding = DATABASE["charset"],
                               pool_recycle = DATABASE["pool_recycle"])
        Tables.meta.reflect(self.e)

    def __getattr__(self, name):
        try:
            return Tables.meta.tables[name]
        except KeyError:
            raise exc.NoSuchTableError(name)

    def execute(self, *args, **kwargs):
        return self.e.execute(*args, **kwargs)

table = Tables()