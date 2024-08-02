s='02:56:04AM'
s1=s.split(':')
s2=[]
if 'PM' in s1[2]:
    for j in s1[:2]:
        s2.append(int(j))
    s2[0]+=12
    s2.append(s1[2])
    print(f"{s2[0]}:{s2[1]}:{s2[2]}")
else:
    print(s)