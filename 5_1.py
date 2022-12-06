# After the rearrangement procedure completes, what crate ends up on top of each stack?

def main():

    all_lines = []
    with open("5_1_input.txt", "r") as file:
        all_lines = file.read().splitlines()

    stack_lines = []
    instruct_lines = []

    for i in range(len(all_lines)):
        if all_lines[i] == '':
            stack_lines = all_lines[:i]
            instruct_lines = all_lines[i+1:]

    stack_lines = stack_lines[::-1]
    
    stack_indixi = []

    for line in stack_lines:
        print(line)

    for i in range (0, len(stack_lines[0])):
        char = stack_lines[0][i]
        if char.isdigit():
            stack_indixi.append(i)

    stacks_list = [[] for x in range(len(stack_indixi))]

    for line in stack_lines[1:]:
        for i in range(0 , len(stack_indixi)):
            char = line[stack_indixi[i]]
            if char == " ":
                continue
            stacks_list[i].append(char)

    for line in instruct_lines:
        line_instructions = line.split()
        for i in range(0, int(line_instructions[1])):
            # get item from line[3] to line[5]
            picked_up = stacks_list[int(line_instructions[3])-1].pop()
            stacks_list[int(line_instructions[5])-1].append(picked_up)

    for line in stacks_list:
        print(line)

    result = []

    for line in stacks_list:
        result.append(line.pop())

    print("".join(result))
    # print('instructlines', instruct_lines)

    # Result will be a set of letter
    # DKSAW etc.

if __name__=="__main__":
    main()