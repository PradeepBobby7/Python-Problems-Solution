def merge(nums1,nums2):
    result=nums1+nums2
    result.sort()
    result1=[]
    for i in range(0,len(result)+1):
        if result[i]>0:
            result1.append(result[i])
    return result1
print(merge([2,3,4,0,0,0],[6,7,8]))