import math

DICTIONARY = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
def encodeId(num):
    base = len(DICTIONARY)
    encoded = ''

    if num == 0:
        return DICTIONARY[0]
    
    while num > 0:
        encoded += DICTIONARY[(num % base)]
        num = math.floor(num / base)
    
    return encoded[::-1]

def decodeId(id):
    base = len(DICTIONARY)
    decoded = 0

    for i in list(id):
        decoded = decoded * base + DICTIONARY.index(i)

    return decoded

