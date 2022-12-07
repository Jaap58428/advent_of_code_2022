def main():
    lines = []
    
    with open("3_1_input.txt", "r") as file:
        lines = file.read().splitlines()
    
    # find every double letter per row
    # split the row
    total_value = 0

    squad_i = 0
    squad_set = []

    for bag in lines:
        shared_letter = None

        squad_set.append(bag)
        squad_i += 1
        if squad_i > 2:
            print(squad_set)
            shared_letter = set(squad_set[0]).intersection(squad_set[1]).intersection(squad_set[2]).pop()
            print(shared_letter)
            squad_i = 0
            squad_set = []
        
            letter_value = 0
            if shared_letter.islower():
                letter_value = ord(shared_letter) - 96
            else:
                letter_value = ord(shared_letter) - 64 + 26

            total_value += letter_value

    print(total_value)

if __name__=="__main__":    
    main()