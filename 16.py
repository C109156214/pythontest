a1 = input().split(" ")
b1 = input().split(" ")
c1 = input().split(" ")
a2 = input().split(" ")
b2 = input().split(" ")
c2 = input().split(" ")
e=f=g=h=0
if a1 != a2:
    print("兩個矩陣無法相加") 
else:
    e = int(b1[0])+int(b2[0])
    f = int(b1[1])+int(b2[1])
    g = int(c1[0])+int(c2[0])
    h = int(c1[1])+int(c2[1])
    print("-----輸出")
    print(e,f)
    print(g,h)