#!/usr/bin/env python
#-*-coding: utf8-*-

from setuptools import find_packages, setup


install_requires = ['tornado',
					'sqlalchemy']

entry_points = """
	[console_scripts]
	sign_contact = demo.app:run
	insert_admin = demo.scripts.testdata:insert_user
"""

setup(
	name = "sign_contact",
	author = "fatelei@gmail.com",
	version = "0.1",
	install_requires = install_requires,
	entry_points = entry_points,
	packages = find_packages("apps"),
	package_dir = {"": "apps"}
)