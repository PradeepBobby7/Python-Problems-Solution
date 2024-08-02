import random
letters = ['a','c','d','e','f','g','h','i','j','k','l','m','n','o']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['@','#','$','&','*','(',')']
user_let = int(input("How many Letters do you want in your Password : "))
user_num = int(input("How many Numbers do you want in your Password : "))
user_sym = int(input("How many Symbols do you want in your Password : "))

pass_list=[]
for char in range(1,user_let+1):
    pass_list.append(random.choice(letters))
for char in range(1,user_num+1):
    pass_list.append(random.choice(numbers))
for char in range(1,user_sym+1):
    pass_list.append(random.choice(symbols))
random.shuffle(pass_list)
password=""
for char in pass_list:
    password += char
print(password)
