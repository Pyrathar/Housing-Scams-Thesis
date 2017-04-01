
def wordreplacer(array):

    housetype=["flat","apartment","room","house"]

    with open("countries.txt") as f:
        countries = f.readlines()
        countries = [x.strip() and x.split() for x in countries]


        for index, i in enumerate(array):
            if any("HOUSE" in s for s in i):


                for house in housetype:
                    y = array[index]
                    y = [w.replace("HOUSE", house) for w in y]
                    array.append(y)

            #remove ainda nao funciona    array.remove(array[index])


            if any("COUNTRY" in s for s in i):

                for country in countries:
                    y = array[index]
                    y = [w.replace("COUNTRY", country[0]) for w in y]
                    array.append(y)





