stu_scores = input("Write the student scores: ").split()

for n in range(0,len(stu_scores)):
    stu_scores[n]=int(stu_scores[n])

highest_score = 0
for score in stu_scores:
    if score>highest_score:
        highest_score=score
print(f"Your Highest score is {highest_score}")
