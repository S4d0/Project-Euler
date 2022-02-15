"""
Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

"""

string = "How can mirrors be real if our eyes aren't real"
newString = ""

for spaces in string.split(" "):
    newString += spaces.capitalize()
    if len(newString) < len(string):
        newString += " "

string = newString

print(string)