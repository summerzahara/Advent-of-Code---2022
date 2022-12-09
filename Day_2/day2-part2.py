def rock_paper_scissors():
    with open("rps.txt", "r") as f:
        file = f.read().strip()
        arr = file.split("\n")
    one_score = 0
    two_score = 0
    for item in arr:
        if  item[2] == "X":
            one, two = evaluate(item[0],lose(item[0]))
            one_score += one
            two_score += two
        elif item[2] == "Y":
            one, two = evaluate(item[0],draw(item[0]))
            one_score += one
            two_score += two
        elif item[2] == "Z":
            one, two = evaluate(item[0],win(item[0]))
            one_score += one
            two_score += two
    print(f"Opponent Score: {one_score}")
    print(f"Your Score: {two_score}")



def evaluate(player1, player2):
    #ROCK: A | X; PAPER: B | Y; SCISSORS C | Z
    if player1 == "A" and player2 == "X":
        player1_score = 1 + 3
        player2_score = 1 + 3
    elif player1 == "A" and player2 == "Y":
        player1_score = 1 + 0
        player2_score = 2 + 6
    elif player1 == "A" and player2 == "Z":
        player1_score = 1 + 6
        player2_score = 3 + 0
    elif player1 == "B" and player2 == "X":
        player1_score = 2 + 6
        player2_score = 1 + 0
    elif player1 == "B" and player2 == "Y":
        player1_score = 2 + 3
        player2_score = 2 + 3
    elif player1 == "B" and player2 == "Z":
        player1_score = 2 + 0
        player2_score = 3 + 6
    elif player1 == "C" and player2 == "X":
        player1_score = 3 + 0
        player2_score = 1 + 6
    elif player1 == "C" and player2 == "Y":
        player1_score = 3 + 6
        player2_score = 2 + 0
    elif player1 == "C" and player2 == "Z":
        player1_score = 3 + 3
        player2_score = 3 + 3
    return player1_score, player2_score


def win(player1):
    if player1 == "A": # ROCK
        player2 = "Y" # PAPER
    elif player1 == "B": # PAPER
        player2 = "Z" # SCISSORS
    elif player1 == "C": # SCISSORS
        player2 = "X" # ROCK
    return player2

def draw(player1):
    if player1 == "A": # ROCK
        player2 = "X" # ROCK
    elif player1 == "B": # PAPER
        player2 = "Y" # PAPER
    elif player1 == "C": # SCISSORS
        player2 = "Z" # SCISSORS
    return player2

def lose(player1):
    if player1 == "A": # ROCK
        player2 = "Z" # SCISSORS
    elif player1 == "B": # PAPER
        player2 = "X" # ROCK
    elif player1 == "C": # SCISSORS
        player2 = "Y" # PAPER
    return player2


rock_paper_scissors()
