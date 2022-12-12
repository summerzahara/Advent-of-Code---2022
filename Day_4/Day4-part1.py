
def assignment():
    with open("day4.txt", "r") as f:
        file = f.read().strip()
        arr = file.split("\n")
    # print(arr)

    count = 0
    false_ = 0
    for item in arr:
        a, b = range_pair(item)
        c = compare_arr(a,b)
        if c == True:
            count += 1
        else:
            false_ += 1
    print(count)
    # print(false_)
    # print(count + false_)




def range_pair(string):
    item_tuple = tuple(string.split(","))
    range1 = []
    range2 = []
    for i in item_tuple:
        one = item_tuple[0].split("-")
        two = item_tuple[1].split("-")
        for i in range(int(one[0]),int(one[1])+1):
            range1.append(i)
        for i in range(int(two[0]),int(two[1])+1):
            range2.append(i)
    # print(f"Range 1: {range1}")
    # print(f"Range 2: {range2}")
    # print(one, two)
    return range1, range2
item = '11-73,29-73'
item2 = '2-8,3-7'
item3 = '6-6,4-6'
#a, b = range_pair(item3)

def compare_arr(arr1, arr2):
    common = []
    for item in arr1:
        if item in arr2:
            common.append(item)
    # print(common)
    if common == arr1:
        # print("True-1")
        return True
    elif common == arr2:
        # print("True-2")
        return True
    else:
        # print("False")
        return False

#compare_arr(a, b)
assignment()
