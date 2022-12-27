def add_score(Difficulty):
    try:
        scores = open('Scores.txt', 'r')

    except FileNotFoundError:
        POINTS_OF_WINNING = (Difficulty * 3) + 5
        scores = open('Scores.txt', 'w')
        scores.writelines(str(POINTS_OF_WINNING))
    else:
        Points_Of_Winning = scores.readline()
        scores.close()