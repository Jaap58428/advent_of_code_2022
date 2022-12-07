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
    highest_index = 0
    for sum in sums:
        if sums[sum] > highest:
            highest = sums[sum]
            highest_index = sum

    print('the highest sum is:', highest)     

if __name__=="__main__":
    main()