from random import randrange

wordDictionary = ['a', 'an','dog', 'cat', 'duck', 'real', 'card', 'car', 'truck', 'word', 'python']
letterDictionary = ['a', 'b', 'c','d', 'e','f','g','h','i','j','k','l','m','n','o','p',
'q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N',
'O','P','Q','R','S','T','U','V','W','X','Y','Z']
numDictionary = ['0', '1', '2', '3', '4', '5','6','7','8','9']
charDictionary = ['!', '@', '#', '$', '%', '^','&','*','-','_','+']

allDict = {0: wordDictionary, 1: letterDictionary, 2: numDictionary, 3: charDictionary}

def buildPassword(allDict, passLength):
    password = ""
    i = 0
    while i < passLength:
        ctype = randrange(4)
        index = randrange(len(allDict[ctype]))
        toolong = True
        while toolong:
            if len(allDict[ctype][index]) <= passLength - i:
                toolong = False
            else:
                index = randrange(len(allDict[ctype]))

        password = password + allDict[ctype][index]
        i = i + len(allDict[ctype][index])

    return password


def main():
    passlength = int(input("Enter password length: "))
    passnum = int(input("Generate how many passwords? "))

    for i in range(passnum):
        passstr = buildPassword(allDict, passlength)
        print(passstr)


if __name__ == "__main__":
    main()

