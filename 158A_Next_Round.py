n, k = map(int,input().split())
 
l = list(map(int,input().split()))
count = 0
for i in l:
         if i == 0:
            break
         elif i >= l[k-1]:
            count += 1
print(count)