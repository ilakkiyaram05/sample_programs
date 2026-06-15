line = input("Enter a sentence: ")

count = {}

for ch in line:

    if ch.isalpha():

        if ch in count:
            count[ch] += 1

        else:
            count[ch] = 1

highest = max(count.values())

result = []

for ch in sorted(count):

    if count[ch] == highest:

        result.append(ch)

print("Highest frequency letters:")

print(*result)
