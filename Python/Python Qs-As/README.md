# **Python Queestions and Solution**

`Q.1` Write a program to find greatest of four number entered by user.

`A.1`

```python
def q_1():
    lst = []
    for x in range(4):
        lst.append(int(input("Enter Number : ")))
    return "Greatest Number : {} among {}.".format(max(lst), lst)
```

---

`Q.2` Write a program to find out whether a student is pass or fail by entered marks of 5 subjects and pass
percentage is greater than equal to 40%.

`A.2`

```Python
def q_2():
    marks = []
    for i in range(5):
        mark = float(input("Enter marks for subject {} : ".format(i + 1)))
        marks.append(mark)

    average = sum(marks) / len(marks)

    if average >= 40:
        return "Congratulations! You have passed."
    else:
        return "Sorry, you have failed."
```

---

`Q.3` Write a program to find whether an email contains `spam text`.

`A.3`

```Python
import re


def q_3():
    spam_keywords = ['enlargement', 'lottery', 'free', 'offer', '1000']

    email = input("Enter email message : ")

    contains_spam = False
    for keyword in spam_keywords:
        if re.search(keyword, email, re.IGNORECASE):
            contains_spam = True
            break

    if contains_spam:
        return "This email contains spam text."
    else:
        return "This email does not contain spam text."
```

---

`Q.4` Write a program to find out whether given username contains less than 10 characters or not.

`A.4`

```Python
def q_4():
    username = input("Enter username: ")

    if len(username) < 10:
        return "The username contains less than 10 characters."
    else:
        return "The username contains 10 or more characters."
```

---

`Q.5` Write a program to find out whether a given name is present in a list or not.

`A.5`

```Python
def q_5():
    names = ['Saksham', 'Kiran', 'Rahul', 'Amardeep', 'Shenankit', 'Hemant', 'Manoj', 'Aayush', 'Vishal']

    name = input("Enter a name: ")

    if name in names:
        return "The name \'{}\' is present in the list.".format(name)
    else:
        return "The name \'{}\' is not present in the list.".format(name)
```

---

`Q.6` Write a program to find whether a given post is talking about `"Someone"` or `"Not"`.

`A.6`

```Python
def q_6():
    import re

    post = input("Enter a post : ")

    if re.search(r'\bsomeone\b', post, re.IGNORECASE):
        return "The post is talking about someone."
    else:
        return "The post is not talking about someone."
```

---

`Q.7` Write a program that asks the user to enter an integer n and displays all the divisors of this number.

`A.7`

```Python
def q_7():
    n = int(input("Enter an integer: "))
    nums = ''

    for i in range(1, n + 1):
        if n % i == 0:
            nums = nums + str(i) + ", "

    return "The divisors of {} are : {}".format(n, nums)
```

---

`Q.8` Write a program in Python, that asks the user to enter an integer `n` and to display the multiplication table of this number.

`A.8`

```Python
def q_8() -> None:
    n = int(input("Enter an integer: "))

    print("Multiplication table of {}:".format(n))

    for i in range(1, 11):
        print("{} x {} = {}".format(n, i, n * i))
    return None
```

---

`Q.9` Write a program to greet all the persons whose names are in a list that start with `'S'`.

```Python
List=["vipin", "hamid", "sapna", "michael", "shoaib", "shreya", "aadil"]
```

`A.9`

```Python
def q_9() -> None:
    names = ["Vipin", "hamid", "sapna", "michael", "shoaib", "shreya", "aadil"]

    for name in names:
        if name.startswith('s' or 'S'):
            print("Hello, {}!".format(name))
    return None

```

---

`Q.10` Write a program that asks the user to enter an integer `'n'` and sends back the message indicating whether the number is `"Prime"` or `"Not"`.

`A.10`

```Python
def q_10() -> str:
    n = int(input("Enter an integer: "))

    if n < 2:
        return "Not Prime"
    else:
        prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                prime = False
                break
        if prime:
            return "Prime"
        else:
            return "Not Prime"
```

---

`Q.11` Write a Python program (use function) that takes as argument two integers `'m'` and `'n'`, and returns the list of all divisors common to `'m'` and `'n'`.

`A.11`

```Python
def q_11() -> list:
    m = int(input("Enter the first integer (m): "))
    n = int(input("Enter the second integer (n): "))

    div_m = {x for x in range(1, m + 1) if m % x == 0}
    div_n = {x for x in range(1, n + 1) if n % x == 0}
    common_divisors = list(div_m & div_n)
    return common_divisors
```

---

`Q.12` Write a Python program (use function) that takes an integer n as an argument and returns the largest and
smallest prime integer less than or equal to n.

`A.12`

```Python
def is_prime(num) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def q_12() -> tuple[int, int]:
    n = int(input("Enter an integer (n): "))

    largest_prime = None
    smallest_prime = None

    for num in range(n, 1, -1):
        if is_prime(num):
            largest_prime = num
            break

    for num in range(n - 1, 1, -1):
        if is_prime(num):
            smallest_prime = num
            break

    return largest_prime, smallest_prime
```

---

`Q.13` Write a program to find the sum of first n natural numbers using both while and for loop.

`A.13`

```Python
def q_13_while() -> int:
    n = int(input("Enter a positive integer (n)[While Loop]: "))

    total = 0
    i = 1

    while i <= n:
        total += i
        i += 1

    return total


def q_13_for() -> int:
    n = int(input("Enter a positive integer (n)[For loop]: "))
    total = 0

    for i in range(1, n + 1):
        total += i

    return total
```

---

`Q.14` Write a program to find factorial of a given number using for loop.

`A.14`

```Python
def q_14() -> int:
    n = int(input("Enter a non-negative integer: "))
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result
```

---

`Q.15` Write a program to print the following star pattern.

```python
# For n = 3 or 4 ...

   *
  * *
 * * *
* * * *
```

`A.15`

```Python
def q_15() -> None:
    n = int(input("Enter a positive integer (n): "))

    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)

    return None
```

---

`Q.16` Write an python program which asks the user to enter an integer `n` and to display a triangle of stars with the
number of rows the integer n typed by the user as shown in the following design:

```Python
# For n = 3 or 4 ...

*
* *
* * *
* * * *
```

`A.16`

```Python
def q_16() -> None:
    n = int(input("Enter a positive integer (n): "))

    for i in range(1, n + 1):
        print("* " * i)

    return None
```

---

`Q.17` Write a program to print the following star pattern.

```Python
# For n = 3 or 4 ...

      *
    * *
  * * *
* * * *
```

`A.17`

```Python
def q_17() -> None:
    n = int(input("Enter a positive integer (n): "))

    for i in range(1, n + 1):
        print(" " * (2 * (n - i)) + "* " * i)
```

---

`Q.18` Write a python program that displays an inverted triangle formed by the digits 0, 1, 2, ... 9 as shown below

```Python
1 2 3 4 5 6 7 8 9 10
2 3 4 5 6 7 8 9 10
3 4 5 6 7 8 9 10
4 5 6 7 8 9 10
5 6 7 8 9 10
6 7 8 9 10
7 8 9 10
8 9 10
9 10
10
```

`A.18`

```Python
def q_18() -> None:
    for i in range(1, 10 + 1):
        for j in range(i, 10 + 1):
            print(j, end=" ")
        print()  # Break

    return None
```

---

`Q.19` Write a program to print the following star pattern.

```Python
* * *
*   *
* * *
```

`A.19`

```Python
def q_19() -> None:
    n = int(input("Enter a positive integer (n): "))

    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
```

---

`Q.20` Write a program to print multiplication table of n using for loop in reversed order.

`A.20`

```Python
def q_20() -> None:
    n = int(input("Enter a positive integer (n): "))

    print("The Multiplication Table of {} :".format(n))
    for i in range(10, 0, -1):
        print(f"{n} x {i} = {n * i}")
    
    return None
```

---

`Q.21`

`A.21`

```Python

```

---

`Q.22`

`A.22`

```Python

```

---

`Q.23`

`A.23`

```Python

```

---

`Q.24`

`A.24`

```Python

```

---

`Q.25`

`A.25`

```Python

```

---

`Q.26`

`A.26`

```Python

```

---

`Q.27`

`A.27`

```Python

```

---

`Q.28`

`A.28`

```Python

```

---

`Q.29`

`A.29`

```Python

```

---

`Q.30`

`A.30`

```Python

```

---

`Q.31`

`A.31`

```Python

```

---

`Q.32`

`A.32`

```Python

```

---

`Q.33`

`A.33`

```Python

```

---

`Q.34`

`A.34`

```Python

```

---

`Q.35`

`A.35`

```Python

```

---

`Q.36`

`A.36`

```Python

```

---

`Q.37`

`A.37`

```Python

```

---

`Q.38`

`A.38`

```Python

```

---

`Q.39`

`A.39`

```Python

```

---

`Q.40`

`A.40`

```Python

```

---

`Q.41`

`A.41`

```Python

```

---

`Q.42`

`A.42`

```Python

```

---

`Q.43`

`A.43`

```Python

```

---

`Q.44`

`A.44`

```Python

```

---

`Q.45`

`A.45`

```Python

```

---

`Q.46`

`A.46`

```Python

```

---

`Q.47`

`A.47`

```Python

```

---

`Q.48`

`A.48`

```Python

```

---

`Q.49`

`A.49`

```Python

```

---

## **Usage**

To run a program, first uncomment the function, then call by run the following command:

```python
print(q_4) # Change question number ...
```

## **Contributing**

Contributions are welcome! If you find any issues with the script or have suggestions for improvements, please open an issue or submit a pull request.

## **License**

This project is Not under any license. Open for all.
