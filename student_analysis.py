import numpy as np

students = np.array([
    [85, 78, 92, 88],
    [70, 65, 72, 75],
    [90, 88, 95, 91],
    [60, 72, 68, 65],
    [82, 90, 85, 87]
])

print("===== STUDENT PERFORMANCE =====")

total_avg = np.mean(students)
print("Average Score:",total_avg);


# for topper and lower student
top_scorrer = 0
top = 0
low = float('inf')
lowest_scorrer = 0
for i in range(len(students)):
    score = np.sum(students[i])
    if score > top:
        top = score
        top_scorrer = i+1

    if score < low:
        low = score
        lowest_scorrer = i+1

print("Topper: Student",top_scorrer);
print("Highest Scorer Marks:",top);
print("Lowest Scorer Marks:",low);


# higest marks in and lowest marks 

arr = students.flatten();
print("Highest Marks:",max(arr));
print("Lowest Marks:",min(arr));

# % student passed

arr1 = np.all(students>=60,axis=1)
passed = np.sum(arr1) / len(students) * 100
print(f"{passed}% Students Passed")


# subject average 

print("===== SUBJECT AVG =====");

avg_sub_marks = np.mean(students, axis=0)
print("Maths:",avg_sub_marks[0])
print("Physics:",avg_sub_marks[1])
print("Chemistry:",avg_sub_marks[2])
print("Computer Science:",avg_sub_marks[3])



