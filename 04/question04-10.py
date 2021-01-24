import turtle

## 전역 변수 부분 ##
num = 0
swidth, sheight = 1000, 300
curX, curY = 0, 0

## 메인 코드 부분 ## 
if __name__ == "__main__" :
    turtle.title("거북이로 2진수 표현하기")
    turtle.shape('turtle')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)
    turtle.penup()
    turtle.left(90)

    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    binNum1 = bin(num1)
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    binNum2 = bin(num2)
    num3 = num1 & num2
    binNum3 = bin(num3)
    print(binNum1)
    print(binNum2)
    print(binNum3)
    curX = swidth / 2
    curY = 100
    for i in range(len(binNum1)-2) :
        turtle.goto(curX,curY)
        if num1 & 1 :
            turtle.color('red')
            turtle.turtlesize(2) 
        else :
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp()
        curX -= 50
        num1 >>= 1 
    
    curX = swidth / 2
    curY = 0
    for i in range(len(binNum2)-2) :
        turtle.goto(curX,curY)
        if num2 & 1 :
            turtle.color('red')
            turtle.turtlesize(2) 
        else :
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp()
        curX -= 50
        num2 >>= 1 

    curX = swidth / 2
    curY = -100
    for i in range(len(binNum3)-2) :
        turtle.goto(curX,curY)
        if num3 & 1 :
            turtle.color('red')
            turtle.turtlesize(2) 
        else :
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp()
        curX -= 50
        num3 >>= 1 

turtle.done()



