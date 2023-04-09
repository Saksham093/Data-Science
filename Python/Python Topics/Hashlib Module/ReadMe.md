# **Python Learning: Hashlib Module 🐍**

## **What is Hashlib?**

This module implements a common interface to many different secure hash and message digest algorithms. The most common hashing algorithm `SHA256`.

Refer for more information from [1. docs.python.org]("https://docs.python.org/3/library/hashlib.html") and [2. geeksforgeeks.org]("https://www.geeksforgeeks.org/hashlib-module-in-python/").The script uses the `hashlib` module to execute the necessary command.

## **Try to Answer**

- [ ] Q. How Hashing is different from encrpyting?
- [ ] Q. Give some practical application.
- [ ] Q. Why some website share `Hash` data. with downloadable file?

## **Usage**

install the module, run the command:

```cli
pip install hashlib
```

The following algorithms are available for hashing:

```python
import hashlib

print(hashlib.algorithms_available)
```

output:

```termainl
{'md5', 'sha256', 'blake2b', 'shake_128', 'shake_256', 'sha3_256', 'blake2s', 'ripemd160', 'sha1', 'md5-sha1', 'sha3_384', 'sha3_512', 'md4', 'sha512_256', 'sm3', 'whirlpool', 'sha512', 'mdc2', 'sha3_224', 'sha224', 'sha512_224', 'sha384'}
```

To execute file, run the following command:

```cli
python main.py
```

>Note: There is one constructor method named for each type of hash. This code is for practice purposes only.

## **Contributing**

Contributions are welcome! If you find any issues with the script or have suggestions for improvements, please open an issue or submit a pull request.

## **License**

This project is Not under any license. Open for all.
