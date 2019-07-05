rj1,rj2=map(int,input().split())
for i in range(rj1+1,rj2):
  for j in range(2,i):
    if(i%j==0):
      break
  else:
    print(i,end=" ")
