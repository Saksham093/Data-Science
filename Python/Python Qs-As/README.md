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

`Q.6` Write a program to find whether a given post is talking about “Someone” or not.

`A.6`

```Python

```

---

`Q.7` Write a program that asks the user to enter an integer n and displays all the divisors of this number.

`A.7`

```Python

```

---

`Q.8` Write a program in Python which asks the user to enter an integer n and to display the multiplication table of
this number.

`A.8`

```Python

```

---

`Q.9` Write a program to greet all the persons whose names in a list which start with `S`.

```Python
List=["vipin", "hamid", "sapna", "michael", "shoaib", "shreya", "aadil"]
```

`A.9`

```Python

```

---

`Q.10` Write a program that asks the user to enter an integer n and sends back the message indicating whether the
number is prime or not.

`A.10`

```Python

```

---

`Q.11` Write a python program (use function)which takes as argument two integers m and n which returns the list
of all divisors common to m and n .

`A.11`

```Python

```

---

`Q.12` Write a python program (use function) that takes an integer n as an argument and returns the largest and
smallest prime integer less than or equal to n.

`A.12`

```Python

```

---

`Q.13` Write a program to find the sum of first n natural numbers using both while and for loop.

`A.13`

```Python

```

---

`Q.14` Write a program to find factorial of a given number using for loop.

`A.14`

```Python

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

```

---

`Q.20` Write a program to print multiplication table of n using for loop in reversed order.

`A.20`

```Python

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

To run a program, first uncomment the funtion, then call by run the following command:

```python
print(q_4) # Change question number ...
```

## **Contributing**

Contributions are welcome! If you find any issues with the script or have suggestions for improvements, please open an issue or submit a pull request.

## **License**

This project is Not under any license. Open for all.
