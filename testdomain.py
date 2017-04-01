from postal.parser import parse_address
import re
from bs4 import BeautifulSoup
import urllib2
from cookielib import CookieJar
import dryscrape





domain = "airbmb.ca"

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent',
                      'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17')]

path = "https://www.webnames.ca/whois#?currentDomain=" + domain

session = dryscrape.Session()
session.visit(path)
response = session.body()
soup = BeautifulSoup(response,)

letters = soup.find_all("div",class_="result ng-binding")

print letters