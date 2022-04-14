"""S_ID: 20CS075 S_NAME: BHARGAVI SAVANI
 Practical6 You are given n words. Some words may repeat. For each word, output its
 number of occurrences. The output order should correspond with the input order
 of appearance of the word. See the sample input/output for clarification."""

n = int(input())
count = {}

for i in range(n):
    word = input()
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(len(count))
print(' '.join([str(count[word]) for word in count]))