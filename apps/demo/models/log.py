#!/usr/bin/env python
#-*-coding: utf8-*-

import time

from sqlalchemy import select

from demo.models.tables import table


class LogDAO(object):
	@classmethod
	def insert_new_log(cls, values):
		values["op_time"] = int(time.time())
		ins = table.log.insert().values(values)
		rst = table.execute(ins)
		_id = rst.inserted_primary_key[0]
		return _id