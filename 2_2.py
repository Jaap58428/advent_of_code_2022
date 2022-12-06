# A = Rock
# B = Paper
# C = Scissors

# X = Lose
# Y = Draw
# Z = Win

def get_my_hand(their_hand, intent):
    # Lose
    if intent == "X":
        if their_hand == "A":
            return "C"
        if their_hand == "B":
            return "A"
        if their_hand == "C":
            return "B"
    # Draw
    if intent == "Y":
        return their_hand
    # Win
    if intent == "Z":
        if their_hand == "A":
            return "B"
        if their_hand == "B":
            return "C"
        if their_hand == "C":
            return "A"
    

def base_score(my_hand):
    if my_hand == "A":
        return 1
    elif my_hand == "B":
        return 2
    elif my_hand == "C":
        return 3
    
def win_score(their_hand, my_hand):
    if their_hand == my_hand:
        return 3
    
    elif their_hand == "A" and my_hand == "B":
        return 6
    elif their_hand == "B" and my_hand == "C":
        return 6
    elif their_hand == "C" and my_hand == "A":
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
    intent = 0
    my_hand = 0

    for game in all_games:
        their_hand, intent = game.split(' ')
        my_hand = get_my_hand(their_hand, intent)
        total_score += base_score(my_hand)
        total_score += win_score(their_hand, my_hand)

    print(total_score)


if __name__=="__main__":
    main()