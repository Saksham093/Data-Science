# Python Projects: Secret Message 🐍
Python Script <br>
This repo contains python code that uses an encryption program to send and receive secret messages with a friend <br>
Run the code.

Python
```python
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
newMessage = ' '

message = input('Please enter a message: ')


for character in message:
    position = alphabet.find(character)
    newPosition = (position + key) % 26
    newCharacter = alphabet[newPosition]
    newMessage += newCharacter
    

print(newMessage)
```

Output
```python
phhwcphcqhducwkhcsdun
```
