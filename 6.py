a = input("輸入值為:").split(",")
a = sorted(a,reverse=True)
b = ""
for i in a:
    b += str(i)
c = int(b)
a.sort()
print(a)
d = ""
for j in a:
    d += str(j)
e = int(d)
print(c-e)  


