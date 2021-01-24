hexNum = input("16진수 한글자 입력 : ")

hexList = ["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","a","b","c","d","e","f"]

if hexNum in hexList :
    num = int(hexNum,16)
    print("10진수 ==> ",num)
else :
    print("16진수가 아닙니다")