n, k = map(int,input().split())
num = list(map(int, input().split()))
 
def main():
 t = k
 tot = k
 if(num[0]==0):
    tot = 0
    print(tot)
    return
 
 if(num[k-1]==0):
    tot = 0
    i = 0
    while(i!=k-1):
        if(num[i]>0):
            tot = tot + 1
            i = i+1
        else:
            break
    print(tot)
    return
 while(t != n):
    if (num[t] >= num[k -1]):
        tot = tot + 1
    t= t + 1
 print(tot)
 
main()
 