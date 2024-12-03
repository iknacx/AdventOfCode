import os
dirname = os.path.dirname(__file__)

with open(f"{dirname}/input.txt") as f:
    source = f.read()

    left = []
    right = []

    for line in source.splitlines():
        nums = line.split("   ")
        left.append(nums[0])
        right.append(nums[1])

    left = sorted(left)
    right = sorted(right)

def part1():
    sum = 0

    for i in range(len(left)):
        sum += abs(int(left[i]) - int(right[i]))

    print(f"part 1: {sum}")

def part2():
    sum = 0

    for n in left:
        sum += int(n) * right.count(n)

    print(f"part 2: {sum}")

if __name__ == "__main__":
    part1()
    part2()
