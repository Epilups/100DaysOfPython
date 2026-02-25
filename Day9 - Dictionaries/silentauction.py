print('Hello. Welcome to the auction')

auction_dictionary = {}

list_complete = False

def add_bid(bid, name):
    auction_dictionary[bid] = name

def get_highest_bidder():
    highest_bid = 0
    highest_bidder_name = ''
    for key in auction_dictionary:
        if key > highest_bid:
            highest_bid = key
            highest_bidder_name = auction_dictionary[key]
    return [highest_bidder_name, highest_bid]

while not list_complete:

    person_name = input('What is your name?: ')
    person_bid = int(input('What is your bid?: $ '))
    add_bid(person_bid, person_name)

    highest_bidder = get_highest_bidder()

    answer = input('Are there any other bidders? Type `yes` or `no` ')
    match answer.lower():
        case 'yes':
            continue
        case 'no':
            print(f'The auction goes to {highest_bidder[0]} with a bid of {highest_bidder[1]}$')
            list_complete = True