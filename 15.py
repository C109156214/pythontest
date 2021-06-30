a = input("輸入一組四位數字為:")
b = list(a)
a1 = int(b[0])
a2 = int(b[1])
a3 = int(b[2])
a4 = int(b[3])

list2 = [7,8,9,0,1,2,3,4,5,6]
total = str(list2[a3])+str(list2[a4])+str(list2[a1])+str(list2[a2])

print("輸出加密後的數字為:"+total)