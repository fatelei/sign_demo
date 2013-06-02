#!/usr/bin/env python
#-*-coding: utf8-*-

import time

from datetime import datetime
from sqlalchemy import select, and_, func

from demo.models.tables import table
from demo.models.user import UserDAO

class CTDAO(object):
    @classmethod
    def insert_new_ct(cls, values):
        values["last_update_time"] = int(time.time())
        ins = table.contract_template.insert().values(values)
        rst = table.execute(ins)
        _id = rst.inserted_primary_key[0]
        return _id


    @classmethod
    def remove_ct(cls, ct_id):
        update = table.contract_template.update()\
                                        .where(table.contract_template.c.id == int(ct_id))\
                                        .values(is_delete = 1)
        table.execute(update)


    @classmethod
    def get_ct_list(cls, page_num, ok_img, delete_img, offset = 20):
        data = []
        query = select([func.count(table.contract_template.c.id)])
        total = table.execute(query).first()[0]
        query_ct = table.contract_template.select()
        query_ct = query_ct.limit(offset)
        query_ct = query_ct.offset((int(page_num) - 1) * offset)
        ct_list = table.execute(query_ct).fetchall()

        for ct in ct_list:
            info = {}
            info["id"] = ct[0]
            info["username"] = UserDAO.get_username_by_id(ct[1])
            info["tpl_name"] = ct[2]
            info["last_update_time"] = datetime.fromtimestamp(ct[5]).strftime("%Y-%m-%d")
            if bool(ct[6]):
                info["is_delete"] = '<img src="{0}"/>'.format(ok_img)
            else:
                info["is_delete"] = '<img src="{0}"/>'.format(delete_img)
            data.append(info)
        per_page_data = {"total": total, "rows": data}