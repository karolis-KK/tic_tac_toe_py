player_x_score = 0
player_o_score = 0

def game_ttt(score_x, score_o):
    while True:
        player_x = input("Player X (1-9): ")
        while True:
            available = None
            available = test_if_available(game, int(player_x))
            if available == True:
                break
            else:
                player_x = input("Spot taken. Player X (1-9): ")
        game[int(player_x) - 1] = "X"
        moves_counter.append(1)
        print(f"{game[0]} | {game[1]} | {game[2]}\n{game[3]} | {game[4]} | {game[5]}\n{game[6]} | {game[7]} | {game[8]}")

        if check_for_win() == "Player X":
            print("Player X won")
            return "Player X won"
        elif check_for_win() == "Player O":
            print("Player O won")
            return "Player O won"
        elif check_for_win() == "Draw":
            print("Draw")
            return "Draw"

        player_o = input("Player O (1-9): ")
        while True:
            available = None
            available = test_if_available(game, int(player_o))
            if available == True:
                break
            else:
                player_o = input("Spot taken. Player O (1-9): ")
        game[int(player_o) - 1] = "O"
        moves_counter.append(1)
        print(f"{game[0]} | {game[1]} | {game[2]}\n{game[3]} | {game[4]} | {game[5]}\n{game[6]} | {game[7]} | {game[8]}")

        if check_for_win() == "Player X":
            print("Player X won")
            return "Player X won"
        elif check_for_win() == "Player O":
            print("Player O won")
            return "Player O won"
        elif check_for_win() == "Draw":
            print("Draw")
            return "Draw"

def test_if_available(game, index):
    if game[index - 1] == " ":
        return True
    else:
        return False
    
def check_for_win():
    if game[0] == "X" and game[1] == "X" and game[2] == "X":
        return "Player X"
    elif game[3] == "X" and game[4] == "X" and game[5] == "X":
        return "Player X"
    elif game[6] == "X" and game[7] == "X" and game[8] == "X":
        return "Player X"
    elif game[0] == "X" and game[3] == "X" and game[6] == "X":
        return "Player X"
    elif game[1] == "X" and game[4] == "X" and game[7] == "X":
        return "Player X"
    elif game[2] == "X" and game[5] == "X" and game[8] == "X":
        return "Player X"
    elif game[0] == "X" and game[4] == "X" and game[8] == "X":
        return "Player X"
    elif game[2] == "X" and game[4] == "X" and game[6] == "X":
        return "Player X"
    elif game[0] == "O" and game[1] == "O" and game[2] == "O":
        return "Player O"
    elif game[3] == "O" and game[4] == "O" and game[5] == "O":
        return "Player O"
    elif game[6] == "O" and game[7] == "O" and game[8] == "O":
        return "Player O"
    elif game[0] == "O" and game[3] == "O" and game[6] == "O":
        return "Player O"
    elif game[1] == "O" and game[4] == "O" and game[7] == "O":
        return "Player O"
    elif game[2] == "O" and game[5] == "O" and game[8] == "O":
        return "Player O"
    elif game[0] == "O" and game[4] == "O" and game[8] == "O":
        return "Player O"
    elif game[2] == "O" and game[4] == "O" and game[6] == "O":
        return "Player O"
    elif len(moves_counter) == 9:
        return "Draw"

while True:
    game = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    moves_counter = []
    won = game_ttt(player_x_score, player_o_score)
    if won == "Player X won":
        player_x_score +=1
    elif won == "Player O won":
        player_o_score +=1
    else:
        pass
    print(f"Player X score: {player_x_score}\nPlayer O score: {player_o_score}")

    choice = input("1. Play again\n2. Quit\n")
    if choice == "2":
        break