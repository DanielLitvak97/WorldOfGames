def add_score(difficulty):
    try:
        file = open("Scores.txt", "r")
        current_score = int(file.readline())
        file.close()
        file = open("Scores.txt", "w")
        file.write(str(current_score + (difficulty * 3) + 5))
        file.close()

    except (IOError, ValueError):
        file = open("Scores.txt", "w")
        file.write(str((difficulty * 3) + 5))
        file.close()

