#!/bin/sh
mkdir days/day$1
touch days/day$1/sol.py
touch days/day$1/example.txt
touch days/day$1/my.txt

echo "#!/usr/local/bin/python3

from pathlib import Path

ex_input = Path(\"days/day$1/example.txt\")
EX_INPUT_STR = ex_input.read_text(encoding=\"utf-8\")

my_input = Path(\"days/day$1/my.txt\")
MY_INPUT_STR = my_input.read_text(encoding=\"utf-8\")


def part1(pz_input):
    return 0

def part2(pz_input):
    return 0

if __name__ == \"__main__\":
    print(\"Day $1 Part 1, Example Output: \", part1(EX_INPUT_STR))
    print(\"Day $1 Part 1, My Output:      \", part1(MY_INPUT_STR))
    print(\"Day $1 Part 2, Example Output: \", part2(EX_INPUT_STR))
    print(\"Day $1 Part 2, My Output:      \", part2(MY_INPUT_STR))" > days/day$1/sol.py

chmod +x days/day$1/sol.py