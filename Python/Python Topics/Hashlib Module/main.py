import hashlib

# To print all the hashing algorithms but some algorithms fromlist may depand on OS
print(hashlib.algorithms_available)

# This list guaranteed, work on your system
# print(hashlib.algorithms_guaranteed)

h = hashlib.new("SHA256")

my_password = "A1b2c3d4@09876"
h.update(my_password.encode())

password_hash = h.hexdigest()
print(password_hash)

user_input = "A1b2c3d4@09876"
h = hashlib.new("SHA256")
h.update(user_input.encode())

input_hash = h.hexdigest()
print(input_hash)

# check
print(password_hash == input_hash)