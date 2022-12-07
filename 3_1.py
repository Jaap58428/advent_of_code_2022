def main():
    lines = []
    
    with open("3_1_input.txt", "r") as file:
        lines = file.read().splitlines()
    
    # find every double letter per row
    # split the row
    total_value = 0

    for bag in lines:
        bagsize = len(bag)
        lefthalf  = bag[0:bagsize//2]
        righthalf = bag[bagsize//2:]

        shared_letter = set(lefthalf).intersection(righthalf).pop()
        
        letter_value = 0
        if shared_letter.islower():
            letter_value = ord(shared_letter) - 96
        else:
            letter_value = ord(shared_letter) - 64 + 26

        total_value += letter_value

    print(total_value)

if __name__=="__main__":    
    main()