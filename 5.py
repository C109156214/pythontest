M=int(input("請輸入階層值Ｍ："))
a=1
b=1
while(a<=M):
    a *= b
    b += 1
print("超過Ｍ為"+str(M)+"的最小階層Ｎ值為："+str(b-1))