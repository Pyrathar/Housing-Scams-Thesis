from postal.parser import parse_address
import re
from bs4 import BeautifulSoup
import urllib2
from cookielib import CookieJar
import urllib, json, time
from nltk.tag import pos_tag

#EMAIL ANALYSIS

def getemail(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    if match is not None:
      email=str(match.group(0))
      return email

def emailsearch(email):

  cj = CookieJar()
  opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
  opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17')]

  path = "http://scammed.by/indexfrom.php?email=" + email
  sourceCode = opener.open(path).read()
  soup = BeautifulSoup(sourceCode,"lxml")


  letters = soup.find_all("div",class_="previewsubject")
  if letters!=[]:
   returnstatement = "http://scammed.by/" + letters[0].a["href"]
   return returnstatement
  else:
   returnstatement ="Not found email is clean"
   return returnstatement

#ADDRESS ANALYSIS

def getaddress(text):
    match = re.search(
        r'\A(.*?)\s+(\d+[a-zA-Z]{0,1}\s{0,1}[-]{1}\s{0,1}\d*[a-zA-Z]{0,1}|\d+[a-zA-Z-]{0,1}\d*[a-zA-Z]{0,1})', text)
    if match is not None:

        print match
        return match
    address = parse_address(text)

    for i in range(len(address)):

        if address[i][1] == "road":
           # print "Road " + address[i][0]
            UserAddress = address[i][0]
            UserAddress.ljust(2)
        if address[i][1] == "house_number":
            if (address[i][0]).isdigit():
               # print "House number" + address[i][0]
                if UserAddress is not None:
                    UserAddress = UserAddress + " " + address[i][0]
                    print UserAddress
        return UserAddress




def AddressGeo(address,api="",delay=5):
  base = r"https://maps.googleapis.com/maps/api/geocode/json?"
  addP = "address=" + address.replace(" ","+")
  GeoUrl = base + addP + "&AIzaSyBhmi4lwBEOzMD9bPNC3ZEnTgy6UAO5ik8=" + api
  response = urllib.urlopen(GeoUrl)
  jsonRaw = response.read()
  jsonData = json.loads(jsonRaw)
  if jsonData['status'] == 'OK':
    resu = jsonData['results'][0]
    finList = [resu['formatted_address'],resu['geometry']['location']['lat'],resu['geometry']['location']['lng']]
  else:
    finList = [None,None,None]
  time.sleep(delay) #in seconds
  return finList

#currency Detection
def getcurrency(text):
    currencies=["dkk","DKK","eur","euros","EUR","EUROS"]
    text=text.split()
    results=[]
    for index, i in enumerate(text):
        for currency in currencies:
            if currency in i != True:
                word=i.replace(currency,"")
                #Words Together Example:4000DKK
                if checkvalue(word) is not False:
                    results.append(word)
                    results.append(currency)

                #Divided Example: 4000 dkk
                if checkvaluesneighboor(text,index) is not False:
                    word = text[index]
                    currency = text[index-1]
                    results.append(word)
                    results.append(currency)

    return results
#checks if it can be converted to value
def checkvalue(value):

    try:
        return int(value)
    except ValueError:
        return False
#Checks if before the index theres a value
def checkvaluesneighboor(text,index):
   try:
       val = int(text[index-1])
       return val
   except ValueError:
       return False

def getuser(text):

    tagged_sent = pos_tag(text.split())

    propernouns = [word for word, pos in tagged_sent if pos == 'NNP']

    return propernouns


