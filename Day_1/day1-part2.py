def top3_max_calories():
    with open("calories.txt", "r") as f:
        file = f.read().strip()
        arr = file.split("\n")

    calories = 0
    one = 0
    two = 0
    three = 0
    for item in arr:
        if item != "":
            cal = int(item)
            calories += cal
            if calories > one:
                three = two
                two = one
                one = calories
            elif calories > two:
                three = two
                two = calories
            elif calories > three:
                three = calories
        else:
            calories = 0
    sum = one + two + three 
    print(f"Elf 1: {one}")
    print(f"Elf 2: {two}")
    print(f"Elf 3: {three}")
    print(f"Total: {sum}")


top3_max_calories() #210406

    