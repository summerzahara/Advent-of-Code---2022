def rock_paper_scissors():
    with open("rps.txt", "r") as f:
        file = f.read().strip()
        arr = file.split("\n")
    one_score = 0
    two_score = 0
    for item in arr:
        #print(f"{item}: {item[0]}, {item[2]}")
        one, two = evaluate(item[0],item[2])
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


rock_paper_scissors()
