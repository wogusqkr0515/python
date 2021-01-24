ch = ""
a,b = 0, 0

while True : 
    a = input("계산할 첫 번째 수를 입력하세요 : ")
    if a == "$" :
        break
    else :
        a = int(a)
    b = int(input("계산할 두 번째 수를 입력하세요 : "))
    ch = input("계산할 연산자를 입력하세요 : ")

    if (ch == "+") :
        print("%d + %d = %d" % (a, b, a+b))
    elif (ch == "-") :
        print("%d - %d = %d" % (a, b, a - b))
    elif (ch == "*") : 
        print("%d * %d = %d" % (a, b, a * b))
    elif (ch ==  "/") :
        print("%d / %d = %d" % (a, b, a / b))
    elif (ch == "%") :
        print("%d %% %d = %d" % (a, b, a % b))
    elif (ch == "//") : 
        print("%d // %d = %d" % (a, b, a // b))
    elif (ch == "**") : 
        print("%d ** %d = %d" % (a, b, a ** b))
    else :
        print("연산자를 잘못 입력했습니다.")

print("$을 입력해 반복문을 탈출했습니다.")