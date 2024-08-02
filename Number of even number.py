def num_even(n):
    result=0
    for i in n:
        i=int(i)
        if i%2==0:
            result+=1
    return result
print(num_even("6382171977"))