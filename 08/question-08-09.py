import turtle
import random
import math
from tkinter.simpledialog import *

inStr = ""
swidth, sheight = 300, 300
tX, tY, txtSize = [0] * 3

turtle.title('거북이 글자쓰기')
turtle.shape('turtle')
turtle.setup(width = swidth + 50, height = sheight + 50)
turtle.screensize(swidth,sheight)
turtle.penup()

inStr = askstring('문자열 입력', '거북이 쓸 문자열을 입력')
lenStr = len(inStr) 
deg = 360 // lenStr 
x,y = 0, 0 
for ch in inStr :
    tX = 100 * math.cos(3.14/180*x)
    tY = 100 * math.sin(3.14/180*y)
    r = random.random(); g = random.random(); b = random.random()

    turtle.goto(tX,tY)

    turtle.pencolor((r,g,b))
    turtle.write(ch, font=('맑은 고딕', 20, 'bold'))
    x += deg; y += deg

turtle.done()