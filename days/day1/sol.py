#!/usr/local/bin/python3

from pathlib import Path

ex_input = Path("days/day1/example.txt")
EX_INPUT_STR = ex_input.read_text(encoding="utf-8")

my_input = Path("days/day1/my.txt")
MY_INPUT_STR = my_input.read_text(encoding="utf-8")

def parse_lists(two_lists):
    left_str  = []
    right_str = []
    for entry in two_lists.split("\n"):
        ll_rl_entry = entry.split("   ")
        left_str.append(ll_rl_entry[0])
        right_str.append(ll_rl_entry[1])

    left_int = [int(str_l_val) for str_l_val in left_str]
    right_int = [int(str_r_val) for str_r_val in right_str]
        
    return left_int, right_int

def part1(pz_input):
    left_list, right_list = parse_lists(pz_input)
    left_list.sort()
    right_list.sort()
    dist = 0 
    for l_val, r_val in zip(left_list, right_list):
        dist += abs(l_val - r_val)
    return dist

def part2(pz_input):
    left_list, right_list = parse_lists(pz_input)
    sim_map = {}
    sim_score = 0
    for l_val in left_list:
        if l_val not in right_list:
            continue # don't need to walk through right list
        
        if l_val not in sim_map: # new val, find num occurrences
            sim_map[l_val] = right_list.count(l_val)

        sim_score += (l_val * sim_map[l_val])
    return sim_score

if __name__ == "__main__":
    print("Day 1 Part 1, Example Output: ", part1(EX_INPUT_STR))
    print("Day 1 Part 1, My Output:      ", part1(MY_INPUT_STR))
    print("Day 1 Part 2, Example Output: ", part2(EX_INPUT_STR))
    print("Day 1 Part 2, My Output:      ", part2(MY_INPUT_STR))
