#!/usr/bin/env python3
import random

text = input("Enter text to be randomly capitalized: ")
result = ""

for i in range (len(text)):
    case = random.randint(0,1)
    if case:
        result += text[i].upper()
    else:
        result += text[i].lower()

print(result)
