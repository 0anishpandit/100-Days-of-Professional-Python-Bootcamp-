student_scores = [150, 160, 170, 180 , 162 , 546 , 65 , 55, 985, 652, 123 , 65 , 666, 55 , 658, 4565 , 45, 5545 ]

# Q1: logic behind sum functionality in library
total_exam_score = sum(student_scores)
print(total_exam_score)

sums = 0

for score in student_scores :
    sums += score

print(sums)

# Q2: logic behind the max functionality in math library
highest_number = max(student_scores)
print(highest_number)

init = student_scores[0]
for highest in student_scores:
    if highest > init :
        init = highest
print(init)


