#!/usr/bin/env python

from distutils.core import setup

setup(name='Distutils',
      version='1.0',
      description='Python Distribution Utilities',
      author='Greg Ward',
      author_email='gward@python.net',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=['json', 'requests','postal.parser','re','bs4','urllib2','cookielib','dryscrape','nltk.tag'],
     )


import re
from bs4 import BeautifulSoup
import urllib2
from cookielib import CookieJar
import urllib, json, time
from nltk.tag import pos_tag

