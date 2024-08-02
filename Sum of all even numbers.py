total=0
for i in range(2,101,2):
    total+=i
print(total)
total2=0
for total1 in range(1,101):
    if total1 %2 ==0:
        total2 +=total1
print(total2)