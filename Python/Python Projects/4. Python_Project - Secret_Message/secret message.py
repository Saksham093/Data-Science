# Python code to demonstrate
# decode()

# initializing string
str = "geeksforgeeks"

# encoding string
str_enc = str.encode(encoding='utf8')

# printing the encoded string
print ("The encoded string in base64 format is : ", str_enc )

# printing the original decoded string
print ("The decoded string is : ",str_enc.decode('utf8', 'strict'))
