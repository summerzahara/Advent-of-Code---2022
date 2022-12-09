def elf_max_calories():
    with open("calories.txt", "r") as f:
        file = f.read().strip()
        arr = file.split("\n")

    calories = 0
    max_cal = 0
    for item in arr:
        if item != "":
            cal = int(item)
            calories += cal
            if calories > max_cal:
                max_cal = calories 
        else:
            calories = 0       
    print(max_cal)

elf_max_calories() #71924

    