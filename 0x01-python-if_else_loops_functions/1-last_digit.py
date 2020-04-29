#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    unid = number % -10
else:
    unid = number % 10
if (unid > 5):
    print("Last digit of", number, "is", unid, "and is greater than 5")
elif (unid == 0):
    print("Last digit of", number, "is", unid, "and is 0")
else:
    print("Last digit of", number, "is", unid, "and is less than 6 and not 0")
