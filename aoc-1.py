def read_input(fpath):

    elf_cals = {}

    with open(fpath, 'r') as infile:
        idx = 0
        for line in infile:
            if line != '\n':
                try: 
                    elf_cals[idx] += int(line)
                except KeyError:
                    elf_cals[idx] = int(line)
            else:
                idx += 1

    return elf_cals

## Part 1
def max_cal(indict):
    elf_idx = max(indict, key=indict.get)

    return elf_idx, indict[elf_idx]



def main():
    fpath = "inputs/aoc-1.txt"
    elf_calories = read_input(fpath)

    ## Part 1
    elf_idx, cal_count = max_cal(elf_calories)

    print(f"Elf with maximum calories is: Elf #{elf_idx + 1}.")
    print(f"Elf {elf_idx + 1} is carrying: {cal_count} calories.")

    ## Part 2
    n = 3
    cal_list = list(elf_calories.values())
    cal_list.sort()
    topn = cal_list[-n:]
    print(f"Total calories of Top {n} elves is {sum(topn)}")


if __name__=="__main__":
    main()





