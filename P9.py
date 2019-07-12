rj,rj1=map(int,input().split())
ct=0
for i in range (rj,rj1+1):
    for j in range(2,i):
        if(i%j==0):
            break
    else: 
        ct+=1
print(ct)
