from string import ascii_lowercase, ascii_uppercase
def rucksack():
    with open("day3.txt", "r") as f:
        file = f.read().strip()
        arr = file.split("\n")
    #print(arr)
    #print(ascii_lowercase)
    priority = []
    for item in arr:
        print(f"array: {item}")
        a, b = split(item)
        c = compare(a,b)
        d = prioritize(c)
        priority.append(d)
    print(f"Priority: {priority}")
    print(f"Length: {len(priority)}")
    n = sum(priority)
    print(n)


def split(input):
    input_arr = []
    for letter in input:
        input_arr.append(letter)
    l = len(input_arr)
    split = int(l/2)
    part1 = []
    part2 = []
    for letter in input_arr[:split]:
        part1.append(letter)
    #print(f"Part 1: {part1}")
    #print(f"Length, p1: {len(part1)}")
    for letter in input_arr[-(split):]:
        part2.append(letter)
    # print(f"Part 2: {part2}")
    # print(f"Length, p2: {len(part2)}")
    return part1, part2

def compare(arr1, arr2):
    #c = []
    for item in arr2:
        if item in arr1:
            #c.append(item)
            c = item
    print(c)
    return c

def prioritize(letter):
    if letter in ascii_lowercase:
        priority = ascii_lowercase.index(letter) + 1
    else:
        priority = ascii_uppercase.index(letter) + 27
    print(priority)
    return priority

rucksack()