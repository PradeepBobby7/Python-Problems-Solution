arr = [1,2,3,4,5,6,7]
print(arr)
r=2
for i in range(0,r):
    position_1=arr[0]
    for j in range(0,len(arr)-1):
        arr[j]=arr[j+1]
    arr[len(arr)-1]=position_1
print(f"Left Rotation: {arr}")
arr1=[1,2,3,4,5,6,7]
r=2
r=-2
len_a=len(arr1)
arr2=arr1[r:len_a]+arr1[0:r]
print(f"Right Rotation: {arr2}")