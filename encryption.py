import random
import string

chars = " "+ string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)
print(f"chars: {chars}")
print( f"key: {key}")
#encrept
plain_text =input("enter plain text: ")
cipher_text = ""
for char in plain_text:
    index = chars.index(char)
    cipher_text += key[index]

print(f"plain text: {plain_text}")
print(f"cipher text: {cipher_text}")
#decrppt
#encrept
cipher_text =input("enter plain text: ")
plain_text = ""
for char in cipher_text:
    index = chars.index(char)
    plain_text += key[index]

print(f"plain text: {plain_text}")
print(f"cipher text: {cipher_text}")