# Problem Statement
Develop a Python program to represent student course registrations using tuples. The program should identify duplicate registrations, detect invalid course combinations based on predefined rules, and determine which students have violated registration rules. Finally, display valid and invalid registrations with appropriate messages.
# Assumptions
1. Each registration is represented as a tuple containing student ID, student name, and course name.
2. A student can register for multiple courses.
3. Duplicate registrations for the same student and course are not allowed.
4. A maximum of 3 courses is allowed per student.
5. Students cannot register for both Python and Java together.
6. Course names are case-insensitive.
7. Invalid registrations are identified and displayed separately.
8. Valid registrations are displayed at the end.
# Algorithm
1. Start.
2. Read the number of registrations.
3. Create an empty list to store registration tuples.
4. Read student ID, name, and course name.
5. Store each registration as a tuple.
6. Convert course names into a common letter case.
7. Check for duplicate registrations.
8. Count the courses registered by each student.
9. Check whether the student has registered for more than 3 courses.
10. Check whether the student has selected both Python and Java.
11. Identify students who violate any registration rule.
12. Display valid registrations and invalid registrations.
13. Stop.
  # mermaid flow chart
  ```mermaid
flowchart TD
    A([Start]) --> B[/Enter Number of Registrations/]
    B --> C[Read Student ID, Name and Course]
    C --> D[Store Registration as Tuple]
    D --> E{More Registrations?}
    E -->|Yes| C
    E -->|No| F[Check Duplicate Registrations]
    F --> G[Group Courses by Student]
    G --> H[Check Maximum Course Limit]
    H --> I[Check Invalid Course Combinations]
    I --> J[Validate Each Registration]
    J --> K{Any Rule Violated?}
    K -->|Yes| L[Add to Invalid List]
    K -->|No| M[Add to Valid List]
    L --> N[Display Valid and Invalid Lists]
    M --> N
    N --> O[Display Students Violating Rules]
    O --> P([Stop])
```
# sample input

Enter number of registrations: 5

Registration 1
Enter Student ID: 101
Enter Student Name: Asha
Enter Course Name: Python

Registration 2
Enter Student ID: 101
Enter Student Name: Asha
Enter Course Name: Java

Registration 3
Enter Student ID: 102
Enter Student Name: Ravi
Enter Course Name: C

Registration 4
Enter Student ID: 102
Enter Student Name: Ravi
Enter Course Name: C

Registration 5
Enter Student ID: 103
Enter Student Name: Priya
Enter Course Name: Python
