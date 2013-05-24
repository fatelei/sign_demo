#!/usr/bin/env python
#-*-coding: utf8-*-

from tornado.options import define

DATABASE = {
    "conn": "mysql://root:123456@localhost/sign_contact",
    "charset": "utf8",
    "pool_recycle": 1800
}

SERVER_PORT = 8888

define("sign_server_port", default = SERVER_PORT, help = "port for server listening")