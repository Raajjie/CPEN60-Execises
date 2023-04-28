#Write a program that allows the user to enter any number of test scores. The user indicate they are done by entering in a negative number. Print how many of the scores are A’s (90 or above). Also print out the average.

scores = []
while True:
    score = float(input("Enter a test score (or a negative number to finish): "))
    if score < 0:
        break
    scores.append(score)

ascores = len([score for score in scores if score >= 90])
ave = sum(scores) / len(scores)

print(f"Number of A's: {ascores}")
print(f"Average score: {ave}")
