import random

allowedStr = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

askLength = int(input("Choose a password length for exmpl. 10, 50, 70 or 8: "))
generatedPass = ""

for i in range(askLength):
    generatedPass += random.choice(allowedStr)

print(generatedPass)