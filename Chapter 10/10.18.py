# Write a program that repeatedly asks the user to enter a football score in the format winning
# score-losing score (like 27-13 or 21-3). The user indicates they are done entering scores by
# entering done. The program should then output the highest score and the lowest score out of
# all the scores entered.

scores = []
while True:
    score = input("Enter a football score (winning score-losing score), or type 'done' to finish: ")
    if score.lower() == 'done':
        break
    else:
        try:
            winning_score, losing_score = map(int, score.split('-'))
            scores.append(winning_score)
            scores.append(losing_score)
        except ValueError:
            print("Invalid input. Please enter scores in the format winning score-losing score.")
            continue

if scores:
    print("Highest score:", max(scores))
    print("Lowest score:", min(scores))
else:
    print("No scores entered.")