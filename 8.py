a = int(input("輸入第一行正整數為："))
b = (input("第二行中數列中的數字為："))
list1 = []

for i in range(0,10):
    c = str(i)
    d = b.count(c)
    list1.append(d)
high = max(list1)
if high <= 1:
    print("每個數字剛好只出現1次")
else:
    for k in range(0,10):
        if list1[k]==high:
            print("最大出現次數的數字為:",k)
            print("出現次數為:",high)
        else:
            continue        
          
