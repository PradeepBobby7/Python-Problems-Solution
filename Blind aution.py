from turtle import clear


logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the secret auction program.")

def check_bit():
    for user in bids:
        high_bid=0
        winner=""
        if high_bid<bids[user]:
            high_bid=bids[user]
            winner=user
    print(f"The winner is {winner} with a bid of ${high_bid}")
bids={}
biding=False
while not biding:
    name=input("What is your name?: ")
    bid=int(input("What's your bid?: $"))
    bids["name"]=bid
    continue_bid=input("Are there any other bidders? Type 'yes' or 'no'.")
    if continue_bid=='no':
        biding=True
        check_bit(bids)
    else:
        clear()