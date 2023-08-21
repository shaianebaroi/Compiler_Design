# INPUT/OUTPUT
reader = open("input.txt", "r")

array = []
for line in reader:
    l = line
    val = l.split()
    array.append(val)
# print(array)

# FUNCTION FOR NUMBERS
def isnum(code):
    try:
        float(code) or int(code)
    except:
        return False
    return True

# STORED ARRAYS
all_keywords = ["if", "float", "elif", "for", "int", "break", "else"]
all_others = [";", ",", "(", ")", "{", "}"]
all_math_operators = ["+", "-", "="]
all_logical_operators = [">", "<"]

# NEW ARRAYS TO STORE DIFFERENT CHARS
keywords = []
others = []
math_operators = []
logical_operators = []
numbers = []
identifiers = []

for count in range(len(array)):
    count2 = 0
    while count2 < len(array[count]):
        code = array[count][count2]

        if code in all_keywords:
            if code not in keywords:
                keywords.append(code)
            array[count].pop(count2)

        elif code in all_others:
            if code not in others:
                others.append(code)
            array[count].pop(count2)

        elif code in all_math_operators:
            if code not in math_operators:
                math_operators.append(code)
            array[count].pop(count2)

        elif code in all_logical_operators:
            if code not in logical_operators:
                logical_operators.append(code)
            array[count].pop(count2)

        elif isnum(code) == True:
            if code not in numbers:
                numbers.append(code)
            array[count].pop(count2)

        else:
            if code not in identifiers:
                identifiers.append(code)
            array[count].pop(count2)

        length2 = len(array[count])

# PRINTING
print("Keywords: ", end="")
print(*keywords, sep=", ")

print("Identifiers: ", end="")
print(*identifiers, sep=", ")

print("Math Operators: ", end="")
print(*math_operators, sep=", ")

print("Logical Operators: ", end="")
print(*logical_operators, sep=", ")

print("Numerical Values: ", end="")
print(*numbers, sep=", ")

print("Others: ", end="")
print(*others, sep=" ")
