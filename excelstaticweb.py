 # -*- coding: utf-8 -*-

from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('sbtmwebport', 'templates'))

template = env.get_template('index.html')