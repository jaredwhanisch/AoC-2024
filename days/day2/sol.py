#!/usr/local/bin/python3

from pathlib import Path

ex_input = Path("days/day2/example.txt")
EX_INPUT_STR = ex_input.read_text(encoding="utf-8")

my_input = Path("days/day2/my.txt")
MY_INPUT_STR = my_input.read_text(encoding="utf-8")

def parse_reports(report_input):
    reports = []
    for r in report_input.split("\n"):
        reports.append(r.split())
    return reports

def part1(pz_input):
    num_safe = 0
    all_reports = parse_reports(pz_input)
    for report in all_reports:
        inc = False
        dec = False
        bigDiff = False
        for i in range(0, len(report)-1):
            curr_int = int(report[i])
            next_int = int(report[i+1])
            diff = abs(curr_int - next_int)

            if diff >= 1 and diff <= 3: 
                if curr_int > next_int and not inc:
                    dec = True
                    inc = False
                elif curr_int < next_int and not dec:
                    inc = True
                    dec = False
                else:
                    inc = False
                    dec = False
                    break
            else:
                bigDiff = True
                break
            
        if (inc or dec) and not bigDiff:
            num_safe += 1
    return num_safe

def part2(pz_input):    
    return 0

if __name__ == "__main__":
    print("Day 2 Part 1, Example Output: ", part1(EX_INPUT_STR))
    print("Day 2 Part 1, My Output:      ", part1(MY_INPUT_STR))
    print("Day 2 Part 2, Example Output: ", part2(EX_INPUT_STR))
    print("Day 2 Part 2, My Output:      ", part2(MY_INPUT_STR))
