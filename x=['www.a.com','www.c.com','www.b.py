x=['www.a.com','www.c.com','www.b.com']
y=[]
for i in x:
    y.append(i.split('.')[1]+'.'+i.split('.')[2])
print(y)