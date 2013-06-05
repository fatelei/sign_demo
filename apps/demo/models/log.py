#!/usr/bin/env python
#-*-coding: utf8-*-

import time

from datetime import datetime
from sqlalchemy import select, and_, func

from demo.models.tables import table


class LogDAO(object):
    @classmethod
    def insert_new_log(cls, values):
        values["op_time"] = int(time.time())
        ins = table.log.insert().values(values)
        rst = table.execute(ins)
        _id = rst.inserted_primary_key[0]
        return _id


    @classmethod
    def get_log_list(cls, page_num, offset = 20):
        data = []
        query = select([func.count(table.log.c.id)])
        total = table.execute(query).first()[0]
        query_log = table.log.select()
        query_log = query_log.limit(offset)
        query_log = query_log.offset((int(page_num) - 1) * offset)
        log_list = table.execute(query_log).fetchall()

        for log in log_list:
            info = {}
            info["id"] = log[0]
            info["op_user"] = log[2]
            info["op_target"] = log[3]
            info["op_time"] = datetime.fromtimestamp(log[1]).strftime("%Y-%m-%d")
            data.append(info)
        per_page_data = {"total": total, "rows": data}
        return per_page_data
