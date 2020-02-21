import random


def main():
    show_header()
    user = input("What is your name? ")
    ai = 'computer'
    play_game(user, ai)


def show_header():
    print('----------------------------')
    print('Rock Paper Scissors V-1     ')
    print('----------------------------')


def play_game(user, ai):
    rounds = 3  # best of 3 series
    wins_p1 = 0  # starts off with 0 rounds
    wins_p2 = 0  # starts off with 0 rounds

    game_rolls = ['rock', 'paper', 'scissors']

    while wins_p1 < rounds and wins_p2 < rounds:
        roll_1 = get_rolls(user, game_rolls)  # asking user for input and making sure input is in the list
        roll_2 = random.choice(game_rolls)  # choosing from the list

        if roll_1 not in game_rolls:
            print("Can't play that, exiting")
            continue

        print(f"{user} rolls {roll_1}")
        print(f"{ai} rolls {roll_2} ")

        winner = check_for_winning_throw(ai, roll_1, roll_2, user)

        if winner is None:
            print("This round was a tie")
        else:
            print(f"{winner} takes this round!")
            if winner == user:
                wins_p1 += 1
            if winner == ai:
                wins_p2 += 1
        print(f"Score is {user}: {wins_p1} and {ai}: {wins_p2}")
        print()

    if wins_p1 >= rounds:
        print(f"{user} wins the game!")
    else:
        print(f"{ai} wins the game!")

    overall_winner = None
    if wins_p1 >= rounds:
        overall_winner = user
    else:
        overall_winner = ai
        print(f"{overall_winner} wins the game!")
        

def check_for_winning_throw(ai, roll_1, roll_2, user):
    # Who wins?
    winner = None
    if roll_1 == roll_2:

        print("Tied play")
    elif roll_1 == "rock":
        if roll_2 == 'paper':
            winner = ai
        elif roll_2 == 'scissors':
            winner = user
    elif roll_1 == 'paper':
        if roll_2 == 'scissors':
            winner = ai
        elif roll_2 == 'rock':
            winner = user
    elif roll_1 == 'scissors':
        if roll_2 == 'rock':
            winner = ai
        elif roll_2 == 'paper':
            winner = user
    return winner


def get_rolls(player_name, rolls):  # rolls from list
    roll = input(f"{player_name}, what is your roll? [rock, paper, or scissors]: ")
    roll = roll.lower().strip()
    if roll not in rolls:  # if roll_1 is not in the list
        print(f"Sorry {player_name}, {roll} is not a valid play!")

    return roll  # returning what user has provided


if __name__ == '__main__':
    main()
