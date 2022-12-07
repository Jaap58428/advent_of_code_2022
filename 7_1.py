# Find all of the directories with a total size of at most 100000. 
# What is the sum of the total sizes of those directories?

def get_input(filename):
    with open(filename, "r") as file:
        return file.read().splitlines()[1:] # skip first line

def is_command(instr):
    return instr[0] == "$"

def main():
    all_instructions = get_input('7_1_input.txt')

    files = {}
    # every dict in dict can be a dir with another dict

    instr_i = 0

    most_recents = []
    current_dir = '/'

    while(True):
        instr = all_instructions[instr_i]

        # check if instruction is a command
        if instr[0] == "$":
            if instr == "$ ls":
                # while the next isntr isnt a command
                while(all_instructions[instr_i + 1][0] != "$"):
                    # list all commands
                    instr_i += 1
                    most_recents.append(all_instructions[instr_i])
                print(most_recents)
                for line in most_recents:
                    a, b = line.split(" ")
                    if a != "dir" and a.isnumeric():
                        files[current_dir] = files[current_dir] + int(a)
                print(files)

            elif instr == "$ cd ..":
                # go one dir up
                pass
       
            elif instr[:4] == "$ cd":
                # go to dir in instr[4:]
                current_dir = instr[4:]
                pass
            
        instr_i += 1
        break

if __name__=="__main__":
    main()