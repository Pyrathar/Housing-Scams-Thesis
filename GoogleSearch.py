import json
import requests

#Experimental filters by .com and .dk
def filtercoms(results):
    link_list = [item["link"] for item in results["items"]]
    for x in link_list:
       if ".dk" in x:
           del link_list[x]
       if ".com" in x:
           del link_list[x]
       if ".org" in x:
           del link_list[x]
       if ".net" in x:
           del link_list[x]

#Prints current list
def process_search(results):
    link_list = [item["link"] for item in results["items"]]
    for x in link_list:
        print x

    return link_list

def Search(searchitem):
    cx = "004907426129582277813:ayzzauq827e"
    key = "AIzaSyBhmi4lwBEOzMD9bPNC3ZEnTgy6UAO5ik8"
    url = "https://www.googleapis.com/customsearch/v1"


    parameters = {"q": searchitem,
                  "cx": cx,
                  "key": key,
                  "searchType": "image"
                  }


    page = requests.request("GET", url, params=parameters)
    results = json.loads(page.text)
    results.keys()

    filtercoms(results)
    currentindex = 0;
    #Doesnt not contain dk or com
    link_list = [item["link"] for item in results["items"]]
    for x in link_list:
        print x



    #Second Research

    #"The best way to hide a body is in the second page of google search"
    while (2>=currentindex):

     next_index = results["queries"]["nextPage"][0]["startIndex"]
     search_terms = results["queries"]["nextPage"][0]["searchTerms"]

     url = "https://www.googleapis.com/customsearch/v1"
     parameters = {"q": search_terms,
                  "cx": cx,
                  "key": key,
                  "start": next_index,
                  "searchType": "image"
                  }

     page = requests.request("GET", url, params=parameters)
     results = json.loads(page.text)
     process_search(results)
     currentindex=currentindex+1


def QuickSearch(searchitem):
    cx = "004907426129582277813:ayzzauq827e"
    key = "AIzaSyBhmi4lwBEOzMD9bPNC3ZEnTgy6UAO5ik8"
    url = "https://www.googleapis.com/customsearch/v1"


    parameters = {"q": searchitem,
                  "cx": cx,
                  "key": key,
                  "searchType": "image"
                  }


    page = requests.request("GET", url, params=parameters)
    results = json.loads(page.text)
    results.keys()
    maxindex = results["searchInformation"]["totalResults"]

    return maxindex






