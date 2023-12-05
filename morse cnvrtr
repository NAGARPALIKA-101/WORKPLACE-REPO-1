def morse(text):
    encrypt = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '!':'-.-.--', 
                    '?':'..--..', '/':'-..-.', '+':'. _ . _ .', 
                    '(':'-.--.', ')':'-.--.-', ' ':' '} 

    decrypt = {value: key for key,value in encrypt.items()}

    if '-' in text:
        return ''.join(decrypt[i]for i in text.split())
    return ''.join(encrypt[i] for i in text.upper())


print("\nYOUR ENTRY")
s = "Anything you want"
print(s)
print("\nYOUR CODED MESSAGE")
print(morse(s))

import subprocess
import time


for character in s:
    if character == "-":
        subprocess.call(["afplay", "F:\VRAJ\VRAJPROGRAMS\dah.wav"])

    if character == ".":
        subprocess.call(["afplay",  "F:\VRAJ\VRAJPROGRAMS\dit.wav"])
    else:
        time.sleep(.1)
