# Day 001 : Skills Assessment

## Table of Contents

- [Day 001 : Skills Assessment](#day-001--skills-assessment)
  - [Table of Contents](#table-of-contents)
  - [Question 1](#question-1)
  - [Question 2](#question-2)
  - [Question 3](#question-3)
  - [Question 4](#question-4)
  - [Question 5](#question-5)
  - [Question 6](#question-6)
  - [Question 7](#question-7)
  - [Question 8](#question-8)
  - [Question 9](#question-9)
  - [Question 10](#question-10)

## Question 1

What's the output for the following code?

```Python
print(len("95637+12"))
```

- [ ] 15
- [ ] 95649
- [ ] 8
- [ ] 95659
- [ ] I don't know.

<details close>

<summary>Correct Answer</summary>

`8`

**Explanation :**
You got it! Proceed to the next question.
</details>

## Question 2

Read the code below, what will be printed in the output?

```Python
score = 67
if score < 80 and score > 70:
    print("A")
elif score < 90 or score > 80:
    print("B")
elif score > 60:
    print("C")
else:
    print("D")
```

- [ ] A
- [ ] B
- [ ] C
- [ ] D

<details close>

<summary>Correct Answer</summary>

`B`

**Explanation :**
You got it! Continue to the next question.
</details>

## Question 3

What will be printed in the console?

```Python
def a_function(a_parameter):    
    a_variable = 15    
    return a_parameter 
a_function(10)
print(a_variable)
```

- [ ] `NameError`
- [ ] 5
- [ ] 10
- [ ] 15

<details close>

<summary>Correct Answer</summary>

`NameError`

**Explanation :**
You got it! Continue to the next question.
</details>

## Question 4

What will be printed as the output?

```Python
def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)

result = outer_function(5, 10)
print(result)
```

- [ ] `SyntaxError`
- [ ] 15
- [ ] 10
- [ ] (5, 10)

<details close>

<summary>Correct Answer</summary>

`15`

**Explanation :**
You got it! Continue to the next question.
</details>

## Question 5

Given a `Car` Class has the following attributes and methods, which line of code in the answers will produce an **error**?

**Attributes:**

`num_of_seats`\
`speed`

**Methods:**

`drive()`\
`break()`

- [ ] `car.drive()`
- [ ] `car.num_of_seats = 2`
- [ ] `car.break = 0`
- [ ] `print(car.speed)`

<details close>

<summary>Correct Answer</summary>

`car.break = 0`

**Explanation :**
You got it! Continue to the next question.
</details>

## Question 6

`my_toyota = Car()`\
`my_fiat = Car()`

What word would you use to describe `my_toyota` and `my_fiat`?

- [ ] `Class`
- [ ] `Attribute`
- [ ] `Object`
- [ ] `Property`
- [ ] `Method`

<details close>

<summary>Correct Answer</summary>

`Object`

**Explanation :**
You got it! Continue to the next question.
</details>

## Question 7

If you are writing code inside the **main.py** file to open the **quiz.txt** what would be the **relative** file path?

- [ ] `"my_files/my_project/quiz.txt"`
- [ ] `"./my_project/quiz.txt"`
- [ ] `"quiz.txt"`
- [ ] `"./quiz"`

<details close>

<summary>Correct Answer</summary>

`"quiz.txt"`

**Explanation :**
You got it! Continue to the next question.
</details>

## Question 8

What is the output of this code?

```Python
def foo(a, b=4, c=6):
    print(a, b, c)

foo(20, c=12)
```

- [ ] `20, 4, 6`
- [ ] No output. This code will generate an error
- [ ] `20, 12`
- [ ] `20, 4, 12`

<details close>

<summary>Correct Answer</summary>

`20, 4, 12`

**Explanation :**
You got it! Continue to the next question.
</details>

## Question 9

What is the output of the code? 

```Python
def all_aboard(a, *args, **kw): 
    print(a, args, kw)

all_aboard(4, 7, 3, 0, x=10, y=64)
```

- [ ] `4 (7, 3, 0) {10, 64}`
- [ ] `4 7 3 0 {'x': 10, 'y': 64}`
- [ ] `4 (7, 3, 0) {'x': 10, 'y': 64}`
- [ ] No output. This code will generate an error
- [ ] `4, 7, 3, 0, x=10, y=64`

<details close>

<summary>Correct Answer</summary>

`4 (7, 3, 0) {'x': 10, 'y': 64}`

**Explanation :**
You got it! Continue to the next question.
</details>

## Question 10

What's the print output for the following code? You do not need a computer to calculate this.

```Python
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num + 3 for num in numbers if num % 2 == 0]
print(result)
```

- [ ] `[1, 1, 5, 3, 5, 8, 13, 21, 34, 55]`
- [ ] `[4, 4, 5, 6, 8, 11, 16, 24, 37, 58]`
- [ ] `[5, 11, 37]`
- [ ] `173`
- [ ] `53`
- [ ] `[4, 4, 6, 8, 16, 24, 58]`

<details close>

<summary>Correct Answer</summary>

`[5, 11, 37]`

**Explanation :**
You got it! Continue to the next question.
</details>

---
