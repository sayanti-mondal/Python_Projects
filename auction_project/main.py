# printing logo
from art import logo

print(logo)

# Find the highest bidder
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"A": 67, "B": 90}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")



bidding_finished = False
bids = {}
while not bidding_finished:
    # Taking inputs from each bidder
    name = input("What is your name?: ")
    price = int(input("What is your bid?: "))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)


