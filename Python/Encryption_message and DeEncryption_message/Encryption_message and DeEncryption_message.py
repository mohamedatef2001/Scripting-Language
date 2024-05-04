import random
import string
all_char = string.digits + string.ascii_letters + string.punctuation + " "
all_char = list(all_char)
key =all_char.copy()
random.shuffle(key)
message=input ("Enter your message : ")
Encryption_message = ""
for letter in message :
    index = all_char.index(letter)
    Encryption_message  += key[index]
print (f"your security message : {Encryption_message}")

print ("*" *180)
DeEncryption_message = ""
for letter in Encryption_message :
    index = key.index(letter)
    DeEncryption_message += all_char[index]
print (f"your DeEncryption messag is : {DeEncryption_message}")
