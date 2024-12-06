import os, math
dirname = os.path.dirname(__file__)



with open(f"{dirname}/input.txt") as f:
    lines = f.read().splitlines()

rules = {}
def readRule(line: str):
    rule = line.split('|')

    if rule[0] in rules:
        rules[rule[0]].append(rule[1])
    else:
        rules[rule[0]] = [rule[1]]


def checkOrder(pages: list[str]) -> tuple[str, int]:
    idx = 0
    while idx < len(pages) - 1:
        if not pages[idx] in rules:
            return pages[idx], len(pages) - 1

        for page in pages[idx + 1:]:

            if not page in rules[pages[idx]]:
                return page, idx

        idx += 1
    return "", -1

def part1() -> list[list[str]]:
    sum = 0
    incorrect = []
    reading_rules = True

    for line in lines:
        if line == "":
            reading_rules = False
            continue

        if reading_rules:
            readRule(line)
        else:
            pages = line.split(',')
            _, idx = checkOrder(pages)
            if idx == -1:
                middle = math.floor(len(pages) / 2)
                sum += int(pages[middle])
            else:
                incorrect.append(pages)

    print(f"part 1: {sum}")
    return incorrect

def part2(incorrect: list[list[str]]):
    sum = 0

    for pages in incorrect:
        while True:
            page, idx = checkOrder(pages)
            if idx == -1:
                middle = math.floor(len(pages) / 2)
                sum += int(pages[middle])
                break

            if idx == len(pages) - 1:
                pages.remove(page)
                pages.append(page)
                continue

            pages.remove(page)
            pages.insert(idx, page)
    
    print(f"part 2: {sum}")

if __name__ == "__main__":
    incorrect = part1()
    part2(incorrect)
