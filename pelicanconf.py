#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Yoel Zeldes'
SITENAME = 'Another Datum'
SITESUBTITLE = 'A blog by Yoel Zeldes'
SITEURL = 'http://localhost:8000'

PATH = 'content'
IGNORE_FILES = ['.ipynb_checkpoints']
DELETE_OUTPUT_DIRECTORY = True

TIMEZONE = 'Israel'
DEFAULT_DATE_FORMAT = '%d %B %Y'
LOCALE = 'en'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('linkedin', 'https://il.linkedin.com/in/yoelzeldes'),
          ('github', 'https://github.com/yoel-zeldes'),
          ('facebook', 'https://www.facebook.com/yoel.zeldes'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

DISQUS_SITENAME = 'anotherdatum'

THEME = './theme'
COLOR_SCHEME_CSS = 'tomorrow.css'
CSS_OVERRIDE = 'css/overrides.css'
HEADER_COVER = 'images/home-bg.jpg'

SUMMARY = True
STATIC_PATHS = ['pages', 'images', 'css']
MENUITEMS = [['Posts', SITEURL]]

