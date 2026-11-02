
import string

# Read paragraph
paragraph = input("Enter a paragraph: ")

# Convert to lowercase
paragraph = paragraph.lower()

# Remove punctuation
for ch in string.punctuation:
    paragraph = paragraph.replace(ch, "")

# Split paragraph into words
words = paragraph.split()

print("\n----- REPEATED WORDS -----")

found = False

# Find repeated words and their positions
for i in range(len(words)):
    word = words[i]

    if word not in words[:i] and words.count(word) > 1:
        positions = []

        for j in range(len(words)):
            if words[j] == word:
                positions.append(j + 1)

        print(word, "Count:", words.count(word),
              "Positions:", positions)
        found = True

if not found:
    print("No repeated words found")

# Find repeated two-word phrases
phrases = []

for i in range(len(words) - 1):
    phrase = words[i] + " " + words[i + 1]

    if phrase not in phrases:
        phrases.append(phrase)

print("\n----- REPEATED PHRASES -----")

found = False

for phrase in phrases:
    count = 0
    positions = []

    for i in range(len(words) - 1):
        current = words[i] + " " + words[i + 1]

        if current == phrase:
            count += 1
            positions.append(i + 1)

    if count > 1:
        print(phrase, "Count:", count,
              "Positions:", positions)
        found = True

if not found:
    print("No repeated phrases found")

