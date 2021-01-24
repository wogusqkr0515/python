## 전역 변수 선언 부분 ##


## 메인 코드 부분 ##
for i in range(0,10) :
    if i < 5 :
        for k in range(1,5-i) : 
            print(' ', end = ' ')
        for k in range(1,2*(i+1)) :
            print('\u2665', end = ' ')
    else :
        for k in range(1,i-3) :
            print(' ', end = ' ')
        for k in range(1,(9-i)*2) :
            print('\u2665', end = ' ')

    print()
   