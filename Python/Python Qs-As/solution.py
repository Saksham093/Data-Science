# Programs ...

# Q.1
# def q_1():
#     lst = []
#     for x in range(4):
#         lst.append(int(input("Enter Number : ")))
#     return "Greatest Number : {} among {}.".format(max(lst), lst)

# ---------------------------------------------------------------------------

# Q.2
# def q_2():
#     marks = []
#     for i in range(5):
#         mark = float(input("Enter marks for subject {} : ".format(i + 1)))
#         marks.append(mark)
#
#     average = sum(marks) / len(marks)
#
#     if average >= 40:
#         return "Congratulations! You have passed."
#     else:
#         return "Sorry, you have failed."

# ---------------------------------------------------------------------------

# import re
#
#
# def q_3():
#     spam_keywords = ['viagra', 'enlargement', 'lottery', 'free', 'offer', '1000']
#
#     email = input("Enter email message : ")
#
#     contains_spam = False
#     for keyword in spam_keywords:
#         if re.search(keyword, email, re.IGNORECASE):
#             contains_spam = True
#             break
#
#     if contains_spam:
#         return "This email contains spam text."
#     else:
#         return "This email does not contain spam text."

# ---------------------------------------------------------------------------

# def q_4():
#     username = input("Enter username: ")
#
#     if len(username) < 10:
#         return "The username contains less than 10 characters."
#     else:
#         return "The username contains 10 or more characters."

# ---------------------------------------------------------------------------

# def q_5():
#     names = ['Saksham', 'Kiran', 'Rahul', 'Amardeep', 'Shenankit', 'Hemant', 'Manoj', 'Aayush', 'Vishal']
#
#     name = input("Enter a name: ")
#
#     if name in names:
#         return "The name \'{}\' is present in the list.".format(name)
#     else:
#         return "The name \'{}\' is not present in the list.".format(name)

# ---------------------------------------------------------------------------

# def q_6():
#     import re
#
#     post = input("Enter a post : ")
#
#     if re.search(r'\bsomeone\b', post, re.IGNORECASE):
#         return "The post is talking about someone."
#     else:
#         return "The post is not talking about someone."

# ---------------------------------------------------------------------------

# def q_7():
#     n = int(input("Enter an integer: "))
#     nums = ''
#
#     for i in range(1, n + 1):
#         if n % i == 0:
#             nums = nums + str(i) + ", "
#
#     return "The divisors of {} are : {}".format(n, nums)


# ---------------------------------------------------------------------------

# def q_8() -> None:
#     n = int(input("Enter an integer: "))
#
#     print("Multiplication table of {}:".format(n))
#
#     for i in range(1, 11):
#         print("{} x {} = {}".format(n, i, n * i))
#     return None


# ---------------------------------------------------------------------------

# def q_9() -> None:
#     names = ["Vipin", "hamid", "sapna", "michael", "shoaib", "shreya", "aadil"]
#
#     for name in names:
#         if name.startswith('s' or 'S'):
#             print("Hello, {}!".format(name))
#     return None


# ---------------------------------------------------------------------------

# def q_10() -> str:
#     n = int(input("Enter an integer: "))
#
#     if n < 2:
#         return "Not Prime"
#     else:
#         prime = True
#         for i in range(2, int(n ** 0.5) + 1):
#             if n % i == 0:
#                 prime = False
#                 break
#         if prime:
#             return "Prime"
#         else:
#             return "Not Prime"


# ---------------------------------------------------------------------------
# def q_11() -> list:
#     m = int(input("Enter the first integer (m): "))
#     n = int(input("Enter the second integer (n): "))
#
#     div_m = {x for x in range(1, m + 1) if m % x == 0}
#     div_n = {x for x in range(1, n + 1) if n % x == 0}
#     common_divisors = list(div_m & div_n)
#     return common_divisors


# ---------------------------------------------------------------------------

# def is_prime(num) -> bool:
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
#
# def q_12() -> tuple[int, int]:
#     n = int(input("Enter an integer (n): "))
#
#     largest_prime = None
#     smallest_prime = None
#
#     for num in range(n, 1, -1):
#         if is_prime(num):
#             largest_prime = num
#             break
#
#     for num in range(n - 1, 1, -1):
#         if is_prime(num):
#             smallest_prime = num
#             break
#
#     return largest_prime, smallest_prime


# ---------------------------------------------------------------------------

# def q_13_while() -> int:
#     n = int(input("Enter a positive integer (n)[While Loop]: "))
#
#     total = 0
#     i = 1
#
#     while i <= n:
#         total += i
#         i += 1
#
#     return total
#
#
# def q_13_for() -> int:
#     n = int(input("Enter a positive integer (n)[For loop]: "))
#     total = 0
#
#     for i in range(1, n + 1):
#         total += i
#
#     return total


# ---------------------------------------------------------------------------

# def q_14() -> int:
#     n = int(input("Enter a non-negative integer: "))
#     result = 1
#
#     for i in range(1, n + 1):
#         result *= i
#
#     return result


# ---------------------------------------------------------------------------

# def q_15() -> None:
#     n = int(input("Enter a positive integer (n): "))
#
#     for i in range(1, n + 1):
#         print(" " * (n - i) + "* " * i)
#
#     return None


# ---------------------------------------------------------------------------

# def q_16() -> None:
#     n = int(input("Enter a positive integer (n): "))
#
#     for i in range(1, n + 1):
#         print("* " * i)
#
#     return None


# ---------------------------------------------------------------------------

# def q_17() -> None:
#     n = int(input("Enter a positive integer (n): "))
#
#     for i in range(1, n + 1):
#         print(" " * (2 * (n - i)) + "* " * i)


# ---------------------------------------------------------------------------

# def q_18() -> None:
#     for i in range(1, 10 + 1):
#         for j in range(i, 10 + 1):
#             print(j, end=" ")
#         print()  # Break
#
#     return None


# ---------------------------------------------------------------------------

# def q_19() -> None:
#     n = int(input("Enter a positive integer (n): "))
#
#     for i in range(n):
#         for j in range(n):
#             if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#                 print("*", end=" ")
#             else:
#                 print(" ", end=" ")
#         print()


# ---------------------------------------------------------------------------

# def q_20() -> None:
#     n = int(input("Enter a positive integer (n): "))
#
#     print("The Multiplication Table of {} :".format(n))
#     for i in range(10, 0, -1):
#         print(f"{n} x {i} = {n * i}")
#
#     return None


# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------


# Call the Function for respective Question ...
print(q_20())
