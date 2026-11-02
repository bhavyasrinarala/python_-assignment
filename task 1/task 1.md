# Problem Statement
Develop a University Scholarship Allocation System to evaluate students based on aggregate marks, subject-wise minimum marks, attendance percentage, and family income. The system checks whether students satisfy all eligibility conditions, calculates their scores, ranks eligible students, and resolves ties using predefined rules. Finally, it displays the scholarship-eligible students in merit order.
# Assumptions
1. Each student has five subjects.
2. Each subject carries 100 marks.
3. Minimum aggregate marks required are 75%.
4. Minimum marks in each subject are 40.
5. Minimum attendance required is 75%.
6. Annual family income must not exceed ₹2,50,000.
7. Students satisfying all conditions are eligible.
8. Eligible students are ranked according to aggregate marks.
9. If aggregate marks are equal, higher attendance gets priority.
10. If both marks and attendance are equal, lower family income gets priority.
# Algorithm
1. Start.
2. Read the number of students.
3. Read each student's name, roll number, five subject marks, attendance, and annual family income.
4. Calculate total marks and aggregate percentage.
5. Check subject-wise minimum marks.
6. Check aggregate percentage, attendance, and income conditions.
7. If all conditions are satisfied, declare the student eligible.
8. Otherwise, declare the student not eligible.
9. Sort eligible students based on:
   - Higher aggregate percentage.
   - Higher attendance.
   - Lower family income.
10. Display the eligible students in rank order.
11. Stop.
 # mermaid flow chart
 ```mermaid
flowchart TD
    A([Start]) --> B[/Enter number of students/]
    B --> C[/Enter student details and marks/]
    C --> D[Calculate total and aggregate percentage]
    D --> E{All subject marks >= 40?}
    E -- No --> I[Declare Not Eligible]
    E -- Yes --> F{Aggregate >= 75%?}
    F -- No --> I
    F -- Yes --> G{Attendance >= 75%?}
    G -- No --> I
    G -- Yes --> H{Income <= 250000?}
    H -- No --> I
    H -- Yes --> J[Declare Eligible]
    J --> K[Rank eligible students]
    I --> L{More students?}
    K --> L
    L -- Yes --> C
    L -- No --> M[Display eligibility and merit list]
    M --> N([Stop])
```
# sample input

Enter number of students: 4

Student 1:
Name: Bhavya
Roll Number: 101
Subject marks: 90 85 88 92 95
Attendance: 90
Annual Income: 200000

Student 2:
Name: Ravi
Roll Number: 102
Subject marks: 80 82 78 85 80
Attendance: 85
Annual Income: 180000

Student 3:
Name: Priya
Roll Number: 103
Subject marks: 70 75 80 78 72
Attendance: 90
Annual Income: 150000

Student 4:
Name: Kiran
Roll Number: 104
Subject marks: 85 90 88 92 87
Attendance: 95
Annual Income: 300000
