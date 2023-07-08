import turtle as t
import math as m
import random as r


def drawX(a, i):
    angle = m.radians(i)
    return a * m.cos(angle)


def drawY(b, i):
    angle = m.radians(i)
    return b * m.sin(angle)



t.bgcolor("#120bdb")
t.setup(1000, 800)
t.penup()
t.goto(150, 0)
t.pendown()
# 1
t.pensize(2)
t.pencolor("white")
t.begin_fill()
for i in range(360):
    x = drawX(150, i)
    y = drawY(60, i)
    t.goto(x, y)
t.fillcolor("#fef5f7")
t.end_fill()
# 2
t.begin_fill()
for i in range(180):
    x = drawX(150, -i)
    y = drawY(70, -i)
    t.goto(x, y)
for i in range(180, 360):
    x = drawX(150, i)
    y = drawY(60, i)
    t.goto(x, y)
t.fillcolor("#f2d7dd")
t.end_fill()
# 3
t.pu()
t.goto(120, 0)
t.pd()
t.begin_fill()
for i in range(360):
    x = drawX(120, i)
    y = drawY(48, i)
    t.goto(x, y)
t.fillcolor("#cbd9f9")
t.end_fill()
# 4
t.begin_fill()
t.pencolor("#fee48c")
for i in range(540):
    x = drawX(120, i)
    y = drawY(48, i) + 70
    t.goto(x, y)
t.goto(-120, 0)
t.fillcolor("#cbd9f9")
t.end_fill()
# 5
t.pu()
t.goto(120, 70)
t.pd()
t.pencolor("#fff0f3")
t.begin_fill()
for i in range(360):
    x = drawX(120, i)
    y = drawY(48, i) + 70
    t.goto(x, y)
t.fillcolor("#fff0f3")
t.end_fill()
# 6
t.pu()
t.goto(110, 70)
t.pd()
t.pencolor("#fff9fb")
t.begin_fill()
for i in range(360):
    x = drawX(110, i)
    y = drawY(44, i) + 70
    t.goto(x, y)
t.fillcolor("#fff9fb")
t.end_fill()
# 14
t.pu()
t.goto(120, 0)
t.pd()
t.begin_fill()
t.pencolor("#ffa79d")
for i in range(180):
    x = drawX(120, -i)
    y = drawY(48, -i) + 10
    t.goto(x, y)
t.goto(-120, 0)
for i in range(180, 360):
    x = drawX(120, i)
    y = drawY(48, i)
    t.goto(x, y)
t.fillcolor("#ffa79d")
t.end_fill()
# 8
t.pu()
t.goto(120, 70)
t.pd()
t.begin_fill()
t.pensize(4)
t.pencolor("#fff0f3")
for i in range(1800):
    x = drawX(120, 0.1 * i)
    y = drawY(-18, i) + 10
    t.goto(x, y)
t.goto(-120, 70)
t.pensize(1)
for i in range(180, 360):
    x = drawX(120, i)
    y = drawY(48, i) + 70
    t.goto(x, y)
t.fillcolor("#fff0f3")
t.end_fill()

t.pu()
t.goto(-56, 180)
t.pd()
t.pencolor("#b1c9e9")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) - 60
    y = drawY(1, i) + 120
    t.goto(x, y)
t.goto(-56, 170)
for i in range(540):
    x = drawX(4, i) - 60
    y = drawY(1, i) + 170
    t.goto(x, y)
t.goto(-64, 120)
t.fillcolor("#b1c9e9")
t.end_fill()
t.pencolor("white")
t.pensize(2)
for i in range(1, 6):
    t.goto(-56, 120 + 10 * i)
    t.pu()
    t.goto(-64, 120 + 10 * i)
    t.pd()
t.pu()
t.goto(-60, 170)
t.pd()
t.goto(-60, 180)
t.pensize(1)
#
t.pu()
t.goto(-56, 190)
t.pd()
t.pencolor("#f1add1")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) - 60
    y = drawY(10, i) + 190
    t.goto(x, y)
t.fillcolor("#f1add1")
t.end_fill()

t.pu()
t.goto(0, 130)
t.pd()
t.pencolor("#b1c9e9")
t.begin_fill()
for i in range(360):
    x = drawX(4, i)
    y = drawY(1, i) + 130
    t.goto(x, y)
t.goto(4, 180)
for i in range(540):
    x = drawX(4, i)
    y = drawY(1, i) + 180
    t.goto(x, y)
t.goto(-4, 130)
t.fillcolor("#b1c9e9")
t.end_fill()
t.pencolor("white")
t.pensize(2)
for i in range(1, 6):
    t.goto(4, 130 + 10 * i)
    t.pu()
    t.goto(-4, 130 + 10 * i)
    t.pd()
t.pu()
t.goto(0, 180)
t.pd()
t.goto(0, 190)
t.pensize(1)
#
t.pu()
t.goto(4, 200)
t.pd()
t.pencolor("#f1add1")
t.begin_fill()
for i in range(360):
    x = drawX(4, i)
    y = drawY(10, i) + 200
    t.goto(x, y)
t.fillcolor("#f1add1")
t.end_fill()
# 16
t.pu()
t.goto(30, 110)
t.pd()
t.pencolor("#b1c9e9")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) + 30
    y = drawY(1, i) + 110
    t.goto(x, y)
t.goto(34, 160)
for i in range(540):
    x = drawX(4, i) + 30
    y = drawY(1, i) + 160
    t.goto(x, y)
t.goto(26, 110)
t.fillcolor("#b1c9e9")
t.end_fill()
t.pencolor("white")
t.pensize(2)
for i in range(1, 6):
    t.goto(34, 110 + 10 * i)
    t.pu()
    t.goto(26, 110 + 10 * i)
    t.pd()
t.pu()
t.goto(30, 160)
t.pd()
t.goto(30, 170)
t.pensize(1)
#
t.pu()
t.goto(34, 180)
t.pd()
t.pencolor("#f1add1")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) + 30
    y = drawY(10, i) + 180
    t.goto(x, y)
t.fillcolor("#f1add1")
t.end_fill()
# 17
t.pu()
t.goto(-30, 110)
t.pd()
t.pencolor("#b1c9e9")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) - 30
    y = drawY(1, i) + 110
    t.goto(x, y)
t.goto(-26, 160)
for i in range(540):
    x = drawX(4, i) - 30
    y = drawY(1, i) + 160
    t.goto(x, y)
t.goto(-34, 110)
t.fillcolor("#b1c9e9")
t.end_fill()
t.pencolor("white")
t.pensize(2)
for i in range(1, 6):
    t.goto(-26, 110 + 10 * i)
    t.pu()
    t.goto(-34, 110 + 10 * i)
    t.pd()
t.pu()
t.goto(-30, 160)
t.pd()
t.goto(-30, 170)
t.pensize(1)
#
t.pu()
t.goto(-26, 180)
t.pd()
t.pencolor("#f1add1")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) - 30
    y = drawY(10, i) + 180
    t.goto(x, y)
t.fillcolor("#f1add1")
t.end_fill()

t.pu()
t.goto(0, 0)
t.fd(-240)
t.left(90)
t.fd(190)
t.pd()
t.write("Happy Birthday ARRTI", font=("Curlz MT", 50))
t.done()


input("Press any key to exit ...")