#!/usr/bin/env python
#-*-coding: utf8-*-

from hashlib import sha1
from struct import pack
from random import getrandbits

def encryption(password):
    if isinstance(password, unicode):
        password = password.encode('utf8')
    salt = pack('I', getrandbits(32))
    digest = sha1(password + salt).digest()
    return (salt + digest).encode('base64')


def check_password(old_password, password):
    if isinstance(password, unicode):
        password = password.encode('utf8')
    old_password = old_password.decode('base64')
    if len(old_password) != 24:
        return False
    salt = old_password[:4]
    digest = old_password[4:]
    if digest != sha1(password + salt).digest():
        return False
    return True


def get_target_module(model, op):
	pass