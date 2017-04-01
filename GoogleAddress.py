from bs4 import BeautifulSoup
import urllib, json, time


#Geolocation of address

def GoogGeoAPI(address,api="",delay=5):
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




#print GoogGeoAPI("weideweltsgade 4")[0]
#0 For complete address,1 lat,2 lng
