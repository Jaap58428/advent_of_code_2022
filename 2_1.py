# A = Rock
# B = Paper
# C = Scissors

# X = Rock
# Y = Paper
# Z = Scissors

def base_score(my_hand):
    if my_hand == "X":
        return 1
    elif my_hand == "Y":
        return 2
    elif my_hand == "Z":
        return 3
    
def win_score(their_hand, my_hand):
    if their_hand == "A" and my_hand == "X":
        return 3
    elif their_hand == "B" and my_hand == "Y":
        return 3
    elif their_hand == "C" and my_hand == "Z":
        return 3
    
    elif their_hand == "A" and my_hand == "Y":
        return 6
    elif their_hand == "B" and my_hand == "Z":
        return 6
    elif their_hand == "C" and my_hand == "X":
        return 6

    else:
        return 0
        
def main():
    print("hey there")
    all_games = []
    with open("2_1_input.txt", "r") as file:
        all_games = file.read().splitlines()

    total_score = 0

    their_hand = 0
    my_hand = 0

    for game in all_games:
        their_hand, my_hand = game.split(' ')
        total_score += base_score(my_hand)
        total_score += win_score(their_hand, my_hand)

    print(total_score)


if __name__=="__main__":
    main()