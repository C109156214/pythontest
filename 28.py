ans = input()
sum = input()
A = 0
B = 0
while sum != "0000":    
    for i in range(0,4):
        for j in range(0,4):
            if sum[i] == ans[j]:
                if i == j:
                    A = A+1            
                else:                   
                    B = B+1
    
    print("%dA%dB"%(A,B))
    A=0
    B=0    
    sum=input()       