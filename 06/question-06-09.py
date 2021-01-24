import turtle
import random

## 전역 변수 선언 부분 ##
color=["blue", "coral", "green", "purple", "yellow"]
swidth, sheight = 700, 700
dist = 5

## 메인 코드 부분 ##

if __name__ == "__main__" :
    turtle.title("거북이 선 그리기")
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)

    t = turtle.Turtle('turtle')
    t.goto(0,0)

    for i in range(80) :
        ran = random.randrange(0,5)
        t.color(color[ran]); t.forward(dist); t.left(30);
        dist += 1 