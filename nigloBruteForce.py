#Niglo BruteForce
import hashlib

print("Password to crack")
password = input()
print("Your password is " + password)

def getMD5Hash(password):
    hashedPassword = hashlib.md5()
    hashedPassword.update(password.encode('utf-8'))
    return str(hashedPassword.hexdigest())

def getSHA256Hash(password):
    hashedPassword = hashlib.sha256()
    hashedPassword.update(password.encode('utf-8'))
    return str(hashedPassword.hexdigest())



