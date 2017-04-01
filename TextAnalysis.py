from difflib import SequenceMatcher
import re, math
from collections import Counter
import Replacer

result=[]
match=0
samplearray=[]

WORD = re.compile(r'\w+')

def wiredtransfers(file):

  words = file.split()
  limit = len(words)-5


  for index, value in enumerate(words):
     if index<limit:
          word1=words[index]
          word2=words[index+1]

          with open("wiredtransfers.txt") as f:
                content = f.readlines()
                content = [x.strip() and x.split() for x in content]

                for index, wired in enumerate(content):

                    if wired[0] == word1 and wired[1] == "null":

                          return word1


                    if wired[0]==word1 and wired[1]==word2:
                          return  word1,word2

def identification(file):

  words = file.split()
  types= ["passport","Passport","id","ID"]

  for i in words:
     for j in types:
         if i==j:
             print i
             return i



def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

def comparebyarray(array):

    with open("Lies.txt") as f:
        content = f.readlines()
        content = [x.strip() and x.split() for x in content]
        Replacer.wordreplacer(content)

        #Lies array
        for j in content:
          str1 = ' '.join(array)
          str2 = ' '.join(j)

          vector1 = text_to_vector(str1)
          vector2 = text_to_vector(str2)


          cosine = get_cosine(vector1, vector2)

          matcher = SequenceMatcher(None, str1,str2).ratio()




          if matcher>=0.80 or cosine >= 0.80:
              print str1




def expressionhunt(file):
    words = file.split()
    limit = len(words)
    samplearray=[]

    for index, value in enumerate(words):
         if index<=(limit-6):
            for i in range(6):

              word = words[index+i]
              samplearray.append(word)


              if i==5:

                comparebyarray(samplearray)
                samplearray=[]
