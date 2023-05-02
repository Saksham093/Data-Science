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
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------


# Call the Function for respective Question ...
# print(q_5())
