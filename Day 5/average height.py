# Input a Python list of student heights.
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
avg = 0
sum = 0
for i in student_heights:
    sum += i
    avg = round(sum / len(student_heights))
print(f"total height = {sum}\nnumber of students = {len(student_heights)}\naverage height = {avg}")
