rj=int(input())
if rj>1:
  for i in range(2,rj):
    if rj%i==0:
      print("no")
      break
  else:
    print("yes")
      
else:
  print("no")
