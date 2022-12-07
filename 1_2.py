def main():
    lines = []

    with open("1_1_input.txt", "r") as file:
        lines = file.read().splitlines()

    # create list of sums
    index = 0
    sums = {}
    temp_sum = 0
    for line in lines:
        if line == '':
            sums[index]= temp_sum
            index += 1
            temp_sum = 0
        else:
            temp_sum += int(line)

    # find highest value
    highest = 0
    second_highest = 0
    third_highest = 0

    for isum in sums:
        if sums[isum] > highest:
            third_highest = second_highest
            second_highest = highest
            highest = sums[isum]
        elif sums[isum] > second_highest:
            third_highest = second_highest
            second_highest = sums[isum]
        elif sums[isum] > third_highest:
            third_highest = sums[isum]
            
    top_three_sum = sum([highest, second_highest, third_highest])

    print('the highest sum is:', top_three_sum)     

if __name__=="__main__":
    main()