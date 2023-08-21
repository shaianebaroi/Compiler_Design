import re

reader = open("input.txt", "r")

n = int(reader.readline())
# print(n)

patterns = []
for count in range(n):
    patterns.append(reader.readline().rstrip("\n"))
# print(patterns)

n = int(reader.readline())
# print(n)

strings = []
for count in range(n):
    strings.append(reader.readline().rstrip("\n"))
# print(strings)

for string in strings:
    for count in range(len(patterns)):
        result = re.match(patterns[count], string)

        if result:
            print("YES,", count + 1)
            break

        else:
            result = False
    if result == False:
        print("NO,", "0")
