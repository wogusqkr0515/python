num1 = int(input(" *** 첫 번째 숫자를 입력하세요 : "))
num2 = int(input(" *** 두 번째 숫자를 입력하세요 : "))
i = int(input(" *** 더할 숫자를 입력하세요 : "))
plus = num1 + i
answer = num1
while plus <num2 + 1 :
    answer = answer + plus
    plus = plus + i
print("%d + %d + ... + %d는 %d입니다. " % (num1,(num1 + i),num2,answer))