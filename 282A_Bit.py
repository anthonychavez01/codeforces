n = int(input())
sum = 0
while(n!=0):
    x = input()  
    if(x == "X++" or x == "++X" ):
       sum = sum +1
    elif(x == "X--" or x == "--X"):
        sum = sum - 1
    n = n - 1
print(sum)