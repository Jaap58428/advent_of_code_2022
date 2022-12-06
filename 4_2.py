# In how many assignment pairs do the ranges overlap?

def is_overlap(e1_low, e1_high, e2_low, e2_high):
    if e1_low <= e2_low and e1_high >= e2_low:
        return True
    
    if e2_low <= e1_low and e2_high >= e1_low:
        return True

def main():

    all_pairs = []
    with open("4_1_input.txt", "r") as file:
        all_pairs = file.read().splitlines()    

    number_of_overlaps = 0

    for pair in all_pairs:
        elf_1, elf_2 = pair.split(",")
        elf_1_lower, elf_1_higher = elf_1.split("-")
        elf_2_lower, elf_2_higher = elf_2.split("-")

        elf_1_lower = int(elf_1_lower)
        elf_1_higher = int(elf_1_higher)
        elf_2_lower = int(elf_2_lower)
        elf_2_higher = int(elf_2_higher)

        if is_overlap(elf_1_lower, elf_1_higher, elf_2_lower, elf_2_higher):
            number_of_overlaps += 1

    print('number_of_overlaps', number_of_overlaps)

if __name__=="__main__":
    main()