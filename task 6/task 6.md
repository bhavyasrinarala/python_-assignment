#  Problem Statement
Develop a Python program to evaluate university applicants based on subject-wise eligibility, aggregate marks, and course-specific minimum thresholds. Select eligible candidates, rank them according to their aggregate marks, and resolve ties using predefined tie-breaking criteria. Finally, generate a ranked list of admitted candidates.
# Assumptions
1. Each candidate has an ID, name, Mathematics, Physics, Chemistry, and aggregate marks.
2. Minimum subject marks required are 40 in each subject.
3. Minimum aggregate marks required are 60%.
4. Course-specific eligibility:
   - CSE: Aggregate must be 75% or above.
   - ECE: Aggregate must be 70% or above.
   - Mechanical: Aggregate must be 65% or above.
5. Candidates who fail subject eligibility are rejected.
6. Candidates are ranked in descending order of aggregate marks.
7. If aggregate marks are equal, Mathematics marks are considered.
8. If Mathematics marks are also equal, candidate ID is used in ascending order.
9. Only eligible candidates are included in the final merit list.
# Algorithm
1. Start.
2. Read the number of applicants.
3. Read the selected course.
4. For each candidate, enter candidate ID, name, and subject marks.
5. Calculate aggregate percentage.
6. Check whether all subject marks are at least 40.
7. Check course-specific aggregate eligibility.
8. If both conditions are satisfied, add the candidate to the eligible list.
9. Sort eligible candidates:
   - Highest aggregate marks first.
   - If aggregate marks are equal, highest Mathematics marks first.
   - If both are equal, lowest candidate ID first.
  # mermaid flow chart
  ```mermaid

flowchart TD
    A([Start]) --> B[/Enter Number of Applicants and Course/]
    B --> C[Set Course-Specific Threshold]
    C --> D[/Enter Candidate ID, Name and Subject Marks/]
    D --> E[Calculate Aggregate Percentage]
    E --> F{All Subject Marks >= 40?}
    F -->|No| G[Reject Candidate]
    F -->|Yes| H{Aggregate >= Course Threshold?}
    H -->|No| G
    H -->|Yes| I[Add Candidate to Eligible List]
    G --> J{More Applicants?}
    I --> J
    J -->|Yes| D
    J -->|No| K[Sort Eligible Candidates]
    K --> L[Apply Tie-Breaking Rules]
    L --> M[Generate Ranked Merit List]
    M --> N[/Display Eligible Candidates and Ranks/]
    N --> O([Stop])
```
# sample input
Enter number of applicants: 4
Enter course (CSE/ECE/Mechanical): CSE

Candidate ID: 101
Candidate Name: Ravi
Mathematics Marks: 90
Physics Marks: 80
Chemistry Marks: 85

Candidate ID: 102
Candidate Name: Priya
Mathematics Marks: 85
Physics Marks: 90
Chemistry Marks: 80

Candidate ID: 103
Candidate Name: Arun
Mathematics Marks: 70
Physics Marks: 75
Chemistry Marks: 80

Candidate ID: 104
Candidate Name: Kiran
Mathematics Marks: 35
Physics Marks: 90
Chemistry Marks: 95
10. Display the ranked merit list.
11. Stop.
