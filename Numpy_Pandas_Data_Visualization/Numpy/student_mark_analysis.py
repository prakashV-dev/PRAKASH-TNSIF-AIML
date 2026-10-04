import numpy as np

marks = np.array([68, 85, 72, 90, 45, 78, 88, 62, 95, 54])
print("Student Marks:", marks)

total_marks = np.sum(marks)
print("Total Marks:", total_marks)

average_marks = np.mean(marks)
print("Average Marks:", average_marks)

highest_mark = np.max(marks)
lowest_mark = np.min(marks)
print("Highest Mark:", highest_mark)
print("Lowest Mark:", lowest_mark)

marks_above_75 = marks[marks > 75]
print("Marks greater than 75:", marks_above_75)
