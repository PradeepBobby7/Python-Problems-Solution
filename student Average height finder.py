stu_height = input("Write the Heights of the Students : ").split()

for n in range(0,len(stu_height)):
    stu_height[n] = int(stu_height[n])
print(stu_height)
total_height=0
for height in stu_height:
    total_height += 1
total=0
for i in stu_height:
    total+=i
average = round(total/total_height)
print(average)