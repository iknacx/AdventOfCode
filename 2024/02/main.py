import os
dirname = os.path.dirname(__file__)

with open(f"{dirname}/input.txt") as f:
    source = f.read()

    reports = []

    for line in source.splitlines():
        levels = line.split(" ")
        levels = list(map(int, levels))
        reports.append(levels)

def isSafe(report: list[int]) -> bool:
    safe = True
    state = 0 # 0: start, 1: increasing, 2: decreasing
    for i in range(len(report) - 1):
        increasing = report[i] < report[i + 1]

        if state == 0:
            state = 1 if increasing else 2

        if (state == 1 and not increasing) or (state == 2 and increasing):
            safe = False
            break

        step = abs(report[i] - report[i + 1])
        if not 0 < step <= 3:
            safe = False
            break
    return safe

def part1() -> tuple[int, list[list[int]]]:
    count = 0
    unsafe = []

    for report in reports:
        if isSafe(report):
            count += 1
        else:
            unsafe.append(report)
    print(f"part 1: {count}")

    return count, unsafe

def part2(count: int, unsafe: list[list[int]]):
    for report in unsafe:
        for i in range(len(report)):
            nr = report[:i]
            nr.extend(report[i + 1:])
            if isSafe(nr):
                count += 1 
                break


    print(f"part 2: {count}")



if __name__ == "__main__":
    count, unsafe = part1()
    part2(count, unsafe)
