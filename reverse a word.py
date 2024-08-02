def reverseWords(s):
    s1=s.split(" ")
    lw=len(s1)
    j=0
    for i in range(0,lw):
        j+=1
        s1[i]=s1[lw-j]
        return print(s1)
        
reverseWords("have a nice day")