import random
def santaSupplier(listOfGivers,listOfRecievers):
    if len(listOfGivers) == 3:
        listOfGiversInStack = listOfGivers
        matchedList = listOfGivers[1:]+[listOfGivers[0]]
        listOfGivers = []
        listOfRecievers = []
        return [f"{listOfGiversInStack[i]} : {matchedList[i]}\n" for i in range(len(matchedList))]
    elif len(listOfGivers) == 0:
        return []
    else:
        giverPicked = random.choice(listOfGivers)
        recieverPicked = random.choice(listOfRecievers)
        while giverPicked == recieverPicked:
            giverPicked = random.choice(listOfGivers)
            recieverPicked = random.choice(listOfRecievers)
        listOfGivers.remove(giverPicked)
        listOfRecievers.remove(recieverPicked)
        return [f"{giverPicked} : {recieverPicked}\n"] + santaSupplier(listOfGivers,listOfRecievers)
with open("names.txt","r") as names:
    names = names.readlines()
    names = [name.rstrip("\n") for name in names]
    with open("santaOutput.txt","w") as output:
        output.writelines(["Giver : Reciever\n"])
        output.writelines(santaSupplier(names,names.copy()))