#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'\u97e9\u5149'
SITENAME = u'\u7b80\u5e90'
SITEURL = 'http://joshuaghost.github.io'

PATH = 'content'
STATIC_PATHS = ['images', 'pdfs', 'blog', 'pages', 'extra']
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# 友情链接 
LINKS = (('宋壬初', 'http://renchusong.github.io/portfolio/'),
         ('Wrfly\'s blog','http://wrfly.kfd.me/'),
         ('Avishek\'s Homepage', 'https://www.l3s.de/~anand/'),
         ('Jaspreet\'s Homepage', 'http://www.l3s.de/~singh/'),)

# Social widget
SOCIAL = (('Fork me on GitHub!', 'http://github.com/JoshuaGhost'),
          ('Twitt me!','http://twitter.com/Joshua_Ghost/'),
          ('Mail me!','zzhang[at]l3s[dot]de'),
          ("My medium page", 'https://medium.com/@zhangzijian0523'))

DEFAULT_PAGINATION = 6

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

USE_FOLDER_AS_CATEGORY = True 
DISPLAY_PAGES_ON_MENU = True

# Custom settings
SUMMARY_MAX_LENGTH = 25
THEME = 'theme/foundation-default-colours/'
PLUGIN_PATHS = ["/home/assassin/workspace/pelican-plugins"]
PLUGINS = ["liquid_tags"]
EXTRA_PATH_METADATA = {'extra/favicon.ico':{'path': 'favicon.ico'}}
