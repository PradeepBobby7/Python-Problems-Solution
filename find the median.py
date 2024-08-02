arr=[56,67,30,79]
arr.sort()
len_ar=len(arr)
if len_ar%2==1:
    mean=len_ar//2
    median=arr[mean]
    return median
elif len_ar%2==0:
    mean1=len_ar//2
    ave=[]
    for i in range(arr[mean1-1],arr[mean1]):
        ave.append(i)
    len_ave=len(ave)
    mean3=len_ave//2
    ans_average=ave[mean3]
    return ans_average

class Solution:
	def find_median(self, v):
		v.sort()
        len_ar=len(v)
        if len_ar%2==1:
            mean=len_ar//2
            median=v[mean]
            return median
        elif len_ar%2==0:
            mean1=len_ar//2
            ave=[]
            for i in range(v[mean1-1],v[mean1]):
                ave.append(i)
            len_ave=len(ave)
            mean3=len_ave//2
            ans_average=ave[mean3]
            return ans_average