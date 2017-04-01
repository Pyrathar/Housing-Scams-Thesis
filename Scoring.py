import TextExtraction
import TextAnalysis
import GoogleSearch


def openfile(filename):
    file = open(filename)
    text = file.read()
    return text


text=openfile("scam2.txt")

#EMAIL ANALYSIS algorithm in TextAnalysis

def emailanalysis(text):

    found = 0

    if (TextExtraction.getemail(text))is not None and found == 0:
        mail = TextExtraction.getemail(text)
        print mail
        response = raw_input("Is the mail of the person? (y/n) ")
        if response == "y":
         print "Searching Databases"
         if TextExtraction.emailsearch(mail)!= "Not found email is clean":
            print "Scammer Found by Email Address"
            found = 1
            return 80
         else:
          print "No email found"
    if found==1:
        return 80

#ADDRESS FINDER AND CHECKER


def addressfinder(text):
    if (TextExtraction.getaddress(text)) is not None:
        address = TextExtraction.getaddress(text)
        print address
        response = raw_input("Is this the address of the house to rent? (y/n) ")
        if response == "y":
         if TextExtraction.AddressGeo(address) is not None:
            print TextExtraction.AddressGeo(address)
            print "Address Exists"
         else:
            print "We could not Lookup the address"
            return 10


#Expression searching
def expressionhunting(text):
    if (TextAnalysis.expressionhunt(text)) is not None:
     print TextAnalysis.expressionhunt(text)
     return 80




#Searches mention of Wired Transfers
def wiredtransfersearch(text):
    #in cash
   if TextAnalysis.wiredtransfers(text) is not None:
    print "Found suspicious behavior"
    return 80


#Search for mentions of Password or ID
def identification(text):
    if TextAnalysis.identification(text) is not None:
        print "WARNING: do not share your passwords or ID online as it may lead to identify theft"
        return 10

    else:
        return "Clean"

#Search for euros and amounts of payment
def searchcurrencyandamount(text):
    filtered=TextExtraction.getcurrency(text)



    for i in filtered:
        if i == "euros":
            response = raw_input("Is the person asking for the payment in Euros? (y/n) ")

            if response == "y":
                print "WARNING: In Denmark you should always discuss in local currency"
                return 20
                break
            else:
                continue

    for index,i in enumerate(filtered):
        i = TextExtraction.checkvalue(i)
        if i is not False and i!=0 and i<3000:
            i=str(i)
            response = raw_input("Does the rent cost " +i+"dkk? (y/n) ")

            if response == "y":
                print "WARNING: Rent seems super cheap and almost impossible to find"
                return 20
                break
            else:
                continue


def ReverseImageAnalysis(imagelink):


   results = GoogleSearch.QuickSearch(imagelink)
   if results>=10:
      return 80
   if GoogleSearch.Search(imagelink) >= 1:
      print GoogleSearch.Search(imagelink)
      return 80






text=openfile("scam2.txt")

Threshold = 0

if Threshold <80:
    #if emailanalysis(text) == 80:
    #    print "Scammer Found By Email"
    #addressfinder(text)
    #expressionhunting(text)
    #wiredtransfersearch(text)
   #identification(text)
   searchcurrencyandamount(text)


