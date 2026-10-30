def find_highest_number(bidding_dictinary):
    highest_bid = 0
    winner = ""

    for bidder in bidding_dictinary:
        bid_amount = bidding_dictinary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of : ₹{highest_bid}")

bids = {}

should_continue = True 
while should_continue: 
    user = input("Enter your name: ") 
    bid = int(input("Enter your Bid Price: ₹ "))
    bids[user] = bid
 
    ask = input("if there are other users who want to bid type 'yes' or 'no': \n").lower()
    if ask == "no":
        should_continue = False 
        find_highest_number(bids)
    elif ask == "yes":
        print("\n"* 20)
        