# aString = "robert"
# reversedString = ""

# print aString.upper()
# print aString.capitalize()

# print aString[::-1]

# aStringAsList = list(aString)
# print aStringAsList.reverse()
# print ''.join(aStringAsList)

# lengthOfString = len(aString)
# print lengthOfString
# for i in range(0,lengthOfString):
#     reversedString += aString[lengthOfString-(i+1)]
# print reversedString

# leetString = "Sean McQuaid"
# newString = leetString.upper()
# print newString.replace("A","4")

# leetDict = {"A": "4","E":"3","G":"6","I":"1","O":"0","S":"5","T":"7"}
# finalString = ""
# for i in range(0,len(newString)):
#     currentLetter = newString[i]
#     if (currentLetter in leetDict):
#         currentLetter = leetDict[currentLetter]
#         finalString += currentLetter
#     print finalString

vowels = "AEIOUaeiou"
numVal = 0
vSet = set(vowels)
rendWord = []
impWord = raw_input("Please enter a word ( ie. Cheese ")
for letter in (impWord):
    if letter in vSet:
        numVAL += 1
        rendWord.append(letter)
        if numVAL == 2:
            rendWord.append((letter)*3)
    else:
        numVAL = 0
        rendWord.append(letter)
wordRendered = "".join(rendWord)
print wordRendered






