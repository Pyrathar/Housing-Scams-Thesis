import Scoring

def openfile(filename):
    file = open(filename)
    text = file.read()
    return text


text = openfile("scamtest.txt")
Threshold = 0

if Threshold<80:

    if Scoring.emailanalysis(text) is not None:
       Threshold=Threshold+80
