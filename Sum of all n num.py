def seriesSum(n):
        answer=0
        for i in range(1,n+1):
            answer=n*(n+1)//2
        return answer
print(seriesSum(6))