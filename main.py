from random import random

def newPassword():
    wordDictionary = ['a', 'an','dog', 'cat', 'duck', 'real', 'card', 'car', 'truck', 'slam', 'timtam']
    letterDictionary = ['a', 'b', 'c','d', 'e','f','g','h','i','j','k','l','m','n','o','p',
    'q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N',
    'O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numDictionary = ['0', '1', '2', '3', '4', '5','6','7','8','9']
    charDictionary = ['!', '@', '#', '$', '%', '^','&','*','-','_','+']

    allDict = {0: wordDictionary, 1: letterDictionary, 2: numDictionary, 3: charDictionary}

    passlength = int(input("Enter password length: "))
    passnum = int(input("Generate how many passwords? "))

    for i in range(passnum):
        passstr = buildPassword(allDict, passlength)+"\n"
        print(passstr)
        print(len(passstr))
    
def buildPassword(allDict, passLength):
    passwordarr = []
    i = 0
    while i < passLength - 1:
        randType = random()
        randIndex = random()
        if randType < 0.25:
            ctype = 0
        elif randType >= 0.25 and randType < 0.50:
            ctype = 1
        elif randType >= 0.50 and randType < 0.75:
            ctype = 2
        else:
            ctype = 3

        index = int((randIndex * 100) % len(allDict[ctype]))
        toolong = True
        while toolong:
            if len(allDict[ctype][index]) < passLength - i:
                toolong = False
            else:
                index = int((random() * 100) % len(allDict[ctype]))

        passwordarr.append(allDict[ctype][index])

        i = 0
        for word in passwordarr:
            i = i + len(word)

    password = ""
    return (password.join(passwordarr))
        
buildPassword()