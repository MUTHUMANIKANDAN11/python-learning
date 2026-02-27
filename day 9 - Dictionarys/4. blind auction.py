auction = {}

while True:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: $"))

    auction[name] = bid
    bidders =input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    print("\n" * 100)
    
    if(bidders == "no"):
        break

max_bid = -1
max_bidder = ""

for name, bid in auction.items():
    if bid > max_bid:
        max_bid = bid
        max_bidder = name
    
print(f"The winner is {max_bidder} with a bid of ${max_bid}")