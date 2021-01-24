layer = int(input("숫자를 입력하세요(1 ~ 5 : "))

now = layer

while now != 1 :
    if now == layer :
        i=0
        star = now*2-1
        while i < star :
            print("*", end = "")
            i = i+1
        print("")
    else :
        i=0
        space = layer - now
        while i < space :
            print(" ", end = "")
            i=i+1
        i=0
        star = now*2-1
        while i < star :
            print("*", end = "")
            i = i+1
        i=0
        while i < space :
            print(" ", end = "")
            i=i+1
        print("")
    now = now - 1 
while now <= layer :
    if now == layer :
        i=0
        star = now*2-1
        while i < star :
            print("*", end = "")
            i = i+1
        print("")
    else :
        i=0
        space = layer - now
        while i < space :
            print(" ", end = "")
            i=i+1
        i=0
        star = now*2-1
        while i < star :
            print("*", end = "")
            i = i+1
        i=0
        while i < space :
            print(" ", end = "")
            i=i+1
        print("")
    now = now + 1

