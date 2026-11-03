n = int(input())
sum = 0
while(n!=0):
    x, y, z =   map(int,input().split())   
    if(x + y + z > 1 ):
       sum = sum +1
    n = n-1
print(sum)