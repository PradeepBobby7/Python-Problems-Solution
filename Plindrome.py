arr=[212,45,313,44]
for i in arr:
    temp=i
    rev=0
    while i>0:
        dig=i%10
        rev=rev*10+dig
        i=i//10
    if temp!=rev:
        print("False")