a = [["123","Tom","DTGD"],["456","Cat","CSIE"],["789","Nana","ASIE"],["321","Lim","DBA"],["654","Won","FDD"]]
s = input("輸入查詢學號為:")
if s==a[0][0]:
    print("學生資料為:"+str(a[0][0])+" "+str(a[0][1])+" "+str(a[0][2]))
elif s==a[1][0]:
    print("學生資料為:"+str(a[1][0])+" "+str(a[1][1])+" "+str(a[1][2]))
elif s==a[2][0]:
    print("學生資料為:"+str(a[2][0])+" "+str(a[2][1])+" "+str(a[2][2]))
elif s==a[3][0]:
    print("學生資料為:"+str(a[3][0])+" "+str(a[3][1])+" "+str(a[3][2]))          
else:
    print("學生資料為:"+str(a[4][0])+" "+str(a[4][1])+" "+str(a[4][2]))  
