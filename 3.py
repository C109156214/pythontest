a = ["rat","ox","tiger","rabbit","dragon","snake","horse","sheep","monkey","rooster","dog","pig"]
year = int(input("輸入西元年："))
ans = (year-4)%12
print(a[ans])