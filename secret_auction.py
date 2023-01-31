#to start use this program please run this commands in order
#1) python3 -m venv venv
#2) pip3 install replit
from replit import clear
from logo import logo 

print(logo)
bid_list = []

#create a function to append the new "item" to the bid list_array
def create_bid_dictionary(name, bid):
    new_bid = {
        "name": name,
        "bid": bid
    }
    bid_list.append(new_bid)

is_bid_finished = False
#looping until the bid is not finished
while not is_bid_finished:
    name_input = input("What's your name?\n").lower()
    bid_input = int(input("What's your offer?\n$"))
    create_bid_dictionary(name=name_input, bid=bid_input)
    terminate_bid_input = input("There are other users who want to bid? Yes/No\n").lower()

    #looping untile the user doesn't enter a valid value
    while terminate_bid_input != 'yes' and terminate_bid_input != 'no':
        print("Please enter valid value")
        terminate_bid_input = input("There are other users who want to bid? Yes/No\n").lower()

    if terminate_bid_input == 'yes':
        clear()
    elif terminate_bid_input == 'no':
        #getting and printing the highest (bid) value inside the bid_list dictionarie's list
        max_bid = max(bid_list, key=lambda x:x["bid"])
        print(f"{max_bid['name']} made the highest offer: {max_bid['bid']}$")
        #the loops stop after the decision of the user (terminate_bid_input)
        is_bid_finished = True

