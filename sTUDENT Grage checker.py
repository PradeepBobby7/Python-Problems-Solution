student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
students_grades={}
for students in student_scores:
    if student_scores[students]>90:
        student_scores[students]="Outstanding"
    elif student_scores[students]>80:
        student_scores[students]="Exceeds Expectation"
    elif student_scores[students]>70:
        student_scores[students]="Acceptable"
    else:
        student_scores[students]="Fail"
students_grades=student_scores
print(students_grades)