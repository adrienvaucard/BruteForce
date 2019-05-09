import hashlib

def getHash(algorithm, password):
    hashedPassword = hashlib.new(algorithm.lower())
    hashedPassword.update(password.encode('utf-8'))
    return str(hashedPassword.hexdigest())
