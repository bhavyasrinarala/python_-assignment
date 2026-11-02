# Problem Statement
Develop a Python program to process a paragraph and identify repeated words and phrases. The program should normalize letter case, count the occurrences of each word using string and list operations, and display repeated words along with their positions in the paragraph.
# Assumptions
1. The paragraph is entered by the user.
2. Uppercase and lowercase letters are treated equally.
3. Punctuation marks are removed before word counting.
4. Words are separated using spaces.
5. Word positions start from 1.
6. A word is considered repeated if it occurs more than once.
7. A phrase is considered repeated if the same consecutive two-word combination occurs more than once.
8. Display the word, occurrence count, and positions.
# Algorithm
1. Start.
2. Read a paragraph from the user.
3. Convert the paragraph into lowercase.
4. Remove punctuation marks.
5. Split the paragraph into individual words.
6. Create an empty list to store repeated words.
# mermaid flow chart
```mermaid
flowchart TD
    A([Start]) --> B[/Enter Paragraph/]
    B --> C[Convert Paragraph to Lowercase]
    C --> D[Remove Punctuation]
    D --> E[Split Paragraph into Words]
    E --> F[Initialize Word Position]
    F --> G[Traverse Word List]
    G --> H[Count Word Occurrences]
    H --> I{Count Greater Than 1?}
    I -->|Yes| J[Identify Word Positions]
    I -->|No| K[Check Next Word]
    J --> L[Display Repeated Word and Positions]
    L --> K
    K --> M{More Words?}
    M -->|Yes| G
    M -->|No| N[Generate Two-Word Phrases]
    N --> O[Count Phrase Occurrences]
    O --> P{Phrase Repeated?}
    P -->|Yes| Q[Display Repeated Phrase and Positions]
    P -->|No| R[Check Next Phrase]
    Q --> R
    R --> S{More Phrases?}
    S -->|Yes| O
    S -->|No| T([Stop])
```
# sample input
Enter a paragraph:
Python is easy and Python is powerful.
Learning Python is easy and learning Python is fun.
