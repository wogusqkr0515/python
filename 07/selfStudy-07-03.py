aa = [[]*4 for i in range(4)]
value = 0
for i in range(4) :
    for k in range(5) :
        aa[i].append(value)
        value += 3
        if aa[i][k] < 10 :
            print(" ", end="")
        print(aa[i][k], end=" ")
    print()

