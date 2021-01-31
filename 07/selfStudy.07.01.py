aa = []
for i in range(10) :
    aa.append(int(input("%d번째 숫자 : " %(i+1))))
hap,k = 0, 0

while k < 10 :
    hap += aa[k]
    k += 1 

print(hap)