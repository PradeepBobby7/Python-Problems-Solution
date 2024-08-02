a=list(map(int,input().split(" ")))
len_a=len(a)
if len_a%2==0:
    b=int(len_a/2)
    b-=1
    print(a[b])
else:
    b=len_a/2
    b-=0.5
    b1=int(b)
    print(a[b1])