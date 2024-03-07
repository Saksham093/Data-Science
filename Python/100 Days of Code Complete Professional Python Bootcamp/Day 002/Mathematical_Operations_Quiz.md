# Day 002 : Mathematical Operations Quiz

## Table of Contents

- [Day 002 : Mathematical Operations Quiz](#day-002--mathematical-operations-quiz)
  - [Table of Contents](#table-of-contents)
  - [Question 1](#question-1)
  - [Question 2](#question-2)
  - [Question 3](#question-3)

## Question 1

You are a computer. What will this line of code print?

```Python
print(6 + 4 / 2 - (1 * 2))
```

- [ ] 3
- [ ] 6.0
- [ ] 8.0
- [ ] 5

<details close>

<summary>Correct Answer</summary>

`6.0`

**Explanation :**
You got it!
</details>

## Question 2

What is the data type of the result of the variable `a` in the following line of code:

```Python
a = int("5") / int(2.7)
```

- [ ] int
- [ ] float
- [ ] str
- [ ] bool

<details close>

<summary>Correct Answer</summary>

`float`

**Explanation :**
int("5") is 5, int(2.7) is 2, so the code becomes: a = 5 ÷ 2 which equals 2.5, which is a float.
</details>

## Question 3

Which of these lines of code will give you an error?

- [ ] .

```Python
name = input("What is your name?")
print(f"Hello, {name}")
```

- [ ] .

```Python
name = input("What is your name?")
print("Hello, " + name)
```

- [ ] .

```Python
age = 12
print(f"You are {age} years old")
```

- [ ] .

```Python
age = 12
print("You are " + age + " years old")
```

<details close>

<summary>Correct Answer</summary>

```Python
age = 12
print("You are " + age + " years old")
```

**Explanation :**
This will give you a Type Error. Age is an integer. You are trying to concatenate a String to an Integer.
</details>

---
