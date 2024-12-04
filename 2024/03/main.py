import os
dirname = os.path.dirname(__file__)

NUMBERS = "1234567890"

with open(f"{dirname}/input.txt") as f:
    source = f.read()


def findMul(idx: int) -> tuple[int, int]:
    fst_num = []
    snd_num = []

    idx = source.find("mul(", idx) + 4

    if idx == 3:
        return 0, idx

    for _ in range(3):
        if source[idx] in NUMBERS:
            fst_num.append(source[idx])
        else:
            break
        idx += 1

    if fst_num == [] or source[idx] != ',':
        return 0, idx

    idx += 1

    for _ in range(3):
        if source[idx] in NUMBERS:
            snd_num.append(source[idx])
        else:
            break
        idx += 1



    if snd_num == [] or source[idx] != ')':
        return 0, idx

    idx += 1

    n1 = int(''.join(fst_num))
    n2 = int(''.join(snd_num))

    return n1 * n2, idx




def part1():
    sum = 0
    idx = 0

    while idx != 3:
        mul, idx = findMul(idx)
        sum += mul

    print(f"part 1: {sum}") 


def part2():
    sum = 0
    idx = 0
    enabled = True
    while idx != 3:
        mul, next_idx = findMul(idx)

        do_idx = source[idx:next_idx].rfind("do()")
        dont_idx = source[idx:next_idx].rfind("don't()")
        if dont_idx != -1 and dont_idx > do_idx:
            enabled = False
        elif do_idx != -1 and do_idx > dont_idx:
            enabled = True

        if enabled:
            sum += mul

        idx = next_idx

    print(f"part 2: {sum}")

if __name__ == "__main__":
    part1()
    part2()
