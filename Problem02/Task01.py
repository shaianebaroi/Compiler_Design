def finder(word):

    # STARTING AT STATE = Q0
    state = "Q0"

    # LOOP FOR EACH LINE
    limit = len(word)

    for count in range(limit):
        element = word[count]

        # CHECKING AT STATE = Q0
        if state == "Q0":
            # IF DIGIT OR .@ IS FOUND, MOVES TO STATE Q8
            if element.isdigit() or element == ".@":
                state = "Q8"
                break
            # IF ALPHABET IS FOUND, MOVES TO Q1
            elif element.isalpha():
                state = "Q1"
                continue

        # CHECKING AT STATE = Q1
        if state == "Q1":
            # IF . IS FOUND, MOVES TO STATE Q3
            if element == ".":
                state = "Q3"
                continue
            # IF ALPHABET IS FOUND, CONTINUES TO THE NEXT ITERATION
            elif element.isalpha():
                continue
            # IF DIGIT OR -_ IS FOUND, MOVES TO STATE Q2
            elif element.isdigit() or element == "-_":
                state = "Q2"
                continue
            # IF @ IS FOUND, MOVES TO STATE Q4
            elif element == "@":
                state = "Q4"
                continue

        # CHECKING AT STATE = Q2
        if state == "Q2":
            # IF @ IS FOUND, MOVES TO STATE Q4
            if element == "@":
                state = "Q4"
                continue
            # IF DIGIT OR ALPHABET OR _- IS FOUND, CONTINUES TO THE NEXT ITERATION
            elif element.isdigit() or element.isalpha() or element == "_-.":
                continue

        # CHECKING AT STATE = Q3
        if state == "Q3":
            # IF ALPHABET OR DIGIT IS FOUND, CONTINUES TO THE NEXT ITERATION
            if element.isalpha() or element.isdigit():
                continue
            # IF @ IS FOUND, MOVES TO STATE Q4
            elif element == "@":
                state = "Q4"
                continue
            # IF . IS FOUND, MOVES TO STATE Q5
            elif element == ".":
                state = "Q5"
                continue

        # CHECKING AT STATE = Q4
        if state == "Q4":
            # IF ALPHABET IS FOUND, CONTINUES TO THE NEXT ITERATION
            if element.isalpha():
                continue
            # IF . IS FOUND, MOVES TO STATE Q6
            elif element == ".":
                state = "Q6"
                continue
            # IF DIGIT OR @_- IS FOUND, MOVES TO STATE Q8
            elif element.isdigit() or element in "@_-":
                state = "Q8"
                break

        # CHECKING AT STATE = Q5
        if state == "Q5":
            # IF ALPHABET IS FOUND, CONTINUES TO THE NEXT ITERATION
            if element.isalpha():
                continue
            # IF DIGIT OR _-. IS FOUND, MOVES TO STATE Q2
            elif element.isdigit() or element in "_-.":
                state = "Q2"
                continue
            # IF @ IS FOUND, MOVES TO STATE Q4
            elif element == "@":
                state = "Q4"
                continue

        # CHECKING AT STATE = Q6
        if state == "Q6":
            # IF ALPHABET IS FOUND, MOVES TO STATE Q7
            if element.isalpha():
                state = "Q7"
                continue
            # OTHERWISE MOVES TO STATE Q8
            else:
                state = "Q8"
                break

        # CHECKING AT STATE = Q7
        if state == "Q7":
            # IF ALPHABET IS FOUND, CONTINUES TO THE NEXT ITERATION
            if element.isalpha():
                continue
            # IF . IS FOUND, MOVES TO STATE Q9
            elif element == ".":
                state = "Q9"
                continue
            # OTHERWISE MOVES TO Q8
            else:
                state = "Q8"
                break

        # CHECKING AT STATE = Q9
        if state == "Q9":
            # IF ALPHABET IS FOUND, MOVES TO STATE Q10
            if element.isalpha():
                state = "Q10"
                continue
            # OTHERWISE MOVES TO Q8
            else:
                state = "Q8"
                break

        # CHECKING AT STATE = Q10
        if state == "Q10":
            # IF ALPHABET IS FOUND, CONTINUES TO THE NEXT ITERATION
            if element.isalpha():
                continue
            # IF . IS FOUND, MOVES TO STATE Q11
            elif element == ".":
                state = "Q11"
                continue
            # OTHERWISE, MOVES TO Q8
            else:
                state = "Q8"
                break

        # CHECKING AT STATE = Q11
        if state == "Q11":
            # IF ALPHABET IS FOUND, MOVES TO STATE Q12
            if element.isalpha():
                state = "Q12"
                continue
            # OTHERWISE, MOVES TO Q8
            else:
                state = "Q8"
                break

        # CHECKING AT STATE = Q12
        if state == "Q12":
            # IF ALPHABET IS FOUND, MOVES TO NEXT ITERATION
            if element.isalpha():
                continue
            # OTHERWISE, MOVES TO STATE Q8
            else:
                state = "Q8"
                break

    # IF THE FINAL STATE IS AT Q5, THEN IT IS A WEBSITE ADDRESS
    if state == "Q5":
        return "Web"

    # ELSE IF THE FINAL STATE IS AT Q7 OR Q10 OR Q12, THEN IT IS AN EMAIL ADDRESS
    elif state == "Q7" or state == "Q10" or state == "Q12":
        return "Email"

    # OTHERWISE, IT IS AN ERROR
    else:
        return "Error"


# INPUT/OUTPUT
reader = open("input.txt", "r")

lines = int(reader.readline())
# print(lines)

# CALLING THE METHOD FOR THE NEXT LINES
for count in range(lines):
    str = reader.readline().rstrip()
    # print(str)
    output = finder(str)
    print(output, ",", count + 1)
