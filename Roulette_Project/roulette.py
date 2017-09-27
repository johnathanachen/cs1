import random

bet_amount = 0
bet_color = None
bet_number = None
random_number = 0
finalized_bet = None
remainder_bankroll = 0
name = "None"
y = "y"
n = "n"

roulette_board = list(range(1,37))

green = [0, 37]
odd = roulette_board[::2] #red
even = roulette_board[1::2] #black
red = odd
black = even
low_numbers = roulette_board[0:18] #1-18
high_numbers = roulette_board[18:36] #19-36
first_dozen = roulette_board[0:12] #1-12
second_dozen = roulette_board[12:24] #13-24
third_dozen = roulette_board[24:36] #25-36

# bets
one_to_one = [low_numbers, even, odd, high_numbers]
two_to_one = [first_dozen, second_dozen, third_dozen]
six_to_one = [green[0], green[1], 1, 2, 3]

'''
red = odd
black = even
'''

# one bet - 35 to 1
# two side bets - 17 to 1
# 11 to 1
# 8 to 1
# 5 to 1

def play_game(bet, amount):

    # take bet
    def check_bet_type(bet):
        bet_type = bet
        finalized_bet = None

        if bet_type == red:
            finalized_bet = red
        elif bet_type == black:
            finalized_bet = black
        elif bet_type == 0:
            finalized_bet = 0
        elif bet_type == 00:
            finalized_bet = 37
        return finalized_bet

    def array_to_name(bet):
        if bet == red:
            name = "red"
        elif bet == black:
            name = "black"
        elif bet == even:
            name = "even"
        elif bet == odd:
            name = "odd"
        elif bet == 0:
            name = "0"
        elif bet == 00:
            name = "00"

        return name

    # roll the ball
    def roll_ball():
        random_number = random.randint(1, 38)
        return random_number

    # check win or lose
    def check_results(amount):
        bank_roll = 1000
        new_bank_roll = 0

        if landed_on in placed_bet:
            new_bank_roll = bank_roll + amount
            print("\nYou won!")
        else:
            new_bank_roll = bank_roll - amount
            print("\nYou Lost, try again!")

        return new_bank_roll

    # Function Calls
    placed_bet = check_bet_type(bet)
    landed_on = roll_ball()
    current_bankroll_amount = check_results(amount)
    name_of_bet = array_to_name(bet)

    print("\nYou picked:")
    print(name_of_bet)

    print("\nThe ball landed on:")
    print(landed_on)

    print("\nYour current bankroll is:")
    print(current_bankroll_amount)

    return 

def replay_game():
    print("\nHow much would you like to bet?")
    amount_placed = input()

    print("\nWhat type of bet would you like to make?")
    print("Choices: even, odd, red, black, 0, or 00")
    bet_choice = input()

    play_game(bet_choice, amount_placed)

    print("\nWould you like to keep playing? (y/n)")
    continue_choice = str(input())

    if continue_choice == "y":
        replay_game()
    else:
        print("good bye")
    return 

def start_game():  
    print("Welcome to Roulette!")
    print("Your starting bankroll is: $1,000")
    print("\nHow much would you like to bet?")
    amount_placed = input()

    print("\nWhat type of bet would you like to make?")
    print("Choices: even, odd, red, black, 0, or 00")
    bet_choice = input()

    play_game(bet_choice, amount_placed)

    print("\nWould you like to keep playing? (y/n)")
    continue_choice = str(input())

    if continue_choice == "y":
        replay_game()
    else:
        print("good bye")
    return    


start_game()

