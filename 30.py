meng = int(input("小明身上有幾元："))
many = int(input("販賣機有幾種飲料："))
list1 = []
for i in range(0,many):
    drink = int(input())
    list1.append(drink)
total = 0
for j in range(0,many):
    if meng >= list1[j]:
        total = total+1
print(total)