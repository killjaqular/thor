# importing the library that holds md5
from hashlib import md5

# getting our random number from the user for proof of concept
randomNumber = input('Enter a random number: ')

# md5 hash of the random number
hashObj = md5(randomNumber.encode())
print(hashObj.hexdigest())
