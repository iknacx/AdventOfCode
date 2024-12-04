const std = @import("std");

const input = @embedFile("input.txt");
const example = @embedFile("example.txt");

const stdout = std.io.getStdOut().writer();

const number_map = std.StaticStringMap(u32).initComptime(.{
    .{ "one", 1 },
    .{ "two", 2 },
    .{ "three", 3 },
    .{ "four", 4 },
    .{ "five", 5 },
    .{ "six", 6 },
    .{ "seven", 7 },
    .{ "eight", 8 },
    .{ "nine", 9 },
});

fn part1() void {
    var lines = std.mem.splitScalar(u8, input, '\n');
    var sum: u32 = 0;
    while (lines.next()) |line| {
        var first: ?u32 = null;
        var last: ?u32 = null;

        for (line) |char| {
            if (std.ascii.isDigit(char)) {
                const num = char - '0';
                if (first == null) {
                    first = num;
                } else {
                    last = num;
                }
            }
        }

        if (first) |f| {
            sum += if (last) |l| f * 10 + l else f * 10 + f;
        }
    }

    stdout.print("part 1: {}\n", .{sum}) catch @panic("Cannot print");
}

fn part2() void {
    var lines = std.mem.splitScalar(u8, input, '\n');
    var sum: u32 = 0;
    var i: usize = 1;
    while (lines.next()) |line| : (i += 1) {
        var first: ?u32 = null;
        var last: ?u32 = null;

        var idx: usize = 0;
        while (idx < line.len) : (idx += 1) {
            if (std.ascii.isDigit(line[idx])) {
                const num = line[idx] - '0';
                if (first == null) {
                    first = num;
                } else {
                    last = num;
                }
            } else {
                for (number_map.keys()) |key| {
                    if (std.mem.startsWith(u8, line[idx..], key)) {
                        // idx += key.len - 1;
                        idx += 1; // fixes ocurrences like twone to match 1 instead of 2

                        if (first == null) {
                            first = number_map.get(key).?;
                        } else {
                            last = number_map.get(key).?;
                        }
                    }
                }
            }
        }

        if (first) |f| {
            sum += if (last) |l| f * 10 + l else f * 10 + f;
        }
    }

    stdout.print("part 2: {}\n", .{sum}) catch @panic("Cannot print");
}

pub fn main() !void {
    part1();
    part2();
}
