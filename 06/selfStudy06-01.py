i, hap = 0, 0

for i in range(0, 101, 1) :
    if i % 7 == 0 :
        hap = hap + i

print("0과 100 사이에 있는 7의 배수 합계 : %d" % hap)