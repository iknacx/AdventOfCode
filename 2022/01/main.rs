fn part1(input: &str) -> Vec<u32> {
    let lines = input.lines();
    let mut elves: Vec<u32> = vec![];

    let mut sum = 0;

    for line in lines {
        if line == "" {
            elves.push(sum);
            sum = 0;
        };

        if let Ok(num) = line.parse::<u32>() {
            sum += num;
        }
    }

    elves.sort();
    elves.reverse();

    println!("part 1: {}", elves[0]);

    return elves;
}

fn part2(elves: Vec<u32>) {
    let total = elves[0] + elves[1] + elves[2];

    println!("part 2: {total}");
}

fn main() {
    let _example = include_str!("./example.txt");
    let input = include_str!("./input.txt");

    let elves = part1(input);
    part2(elves);
}
