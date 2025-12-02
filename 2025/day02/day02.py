from re import match

part1 = part2 = 0

for lo, hi in [
    [int(a) for a in i.split("-")] for i in open("in.txt").read().split(",")
]:
    for num in range(lo, hi + 1):
        if match(r"^(.+)\1$", str(num)):
            part1 += num
        if match(r"^(.+)\1+$", str(num)):
            part2 += num

print("Part 1: ", part1)
print("Part 2: ", part2)
