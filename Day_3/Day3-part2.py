from string import ascii_lowercase, ascii_uppercase

def badges():
    with open("day3.txt", "r") as f:
        file = f.read().strip()
        arr = file.split("\n")

    badge_priority = []
    while int(len(arr)) != 0:
        temp_arr = groups_of_3(arr) # Get first group of 3
        badge = compare(temp_arr) # Find common letter
        p = prioritize(badge) # calculate priority
        badge_priority.append(p) # add to list
        arr = remove_3(arr) # modify original list
    print(badge_priority)
    print(len(badge_priority))
    print(sum(badge_priority))

def groups_of_3(arr):
    temp_arr = []
    for count, item in enumerate(arr):
        if count < 3:
            temp_arr.append(item)
    # print(temp_arr)
    return temp_arr

def remove_3(arr):
    new_arr = arr[3:]
    # print(new_arr)
    return new_arr

def compare(arr):
    first = []
    for item in arr[0]:
        if item in arr[1]:
            first.append(item)
            for item in first:
                if item in arr[2]:
                    c = item
    return c

def prioritize(letter):
    if letter in ascii_lowercase:
        priority = ascii_lowercase.index(letter) + 1
    else:
        priority = ascii_uppercase.index(letter) + 27
    # print(priority)
    return priority

badges()
