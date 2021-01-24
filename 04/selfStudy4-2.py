num = int(input("시프트 할 숫자는? "))
repeat = int(input("출력할 횟수는? "))
result = 0
i = 0

for i in range(1,repeat + 1) :
    result = num << i
    print("%d << %d = %d" % (num, i, result))

for i in range(1,repeat + 1) : 
    result = num >> i
    print("%d >> %d = %d" % (num, i, result))