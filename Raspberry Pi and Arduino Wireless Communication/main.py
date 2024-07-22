prevValue = 0
global myValue
while(1):
    myFile = open("myFile.txt", "rt")
    for lines in myFile:
        for char in lines:
            myValue = int(char)
    myFile.close()
    if prevValue == 0:
        prevValue = myValue
    else:
        if myValue == prevValue + 1:
            prevValue = myValue