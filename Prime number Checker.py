#Write your code below this line 👇
def prime_checker(number):
    prime=True
    for i in range(2,number):
        if number%i == 0:
            prime= False
    if prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
n = int(input("Check this number: "))
prime_checker(number=n)