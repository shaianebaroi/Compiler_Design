reader = open("input.txt", "r")
keywords = ["String"]

# INPUT/OUTPUT
reader = open("input.txt", "r")

array = []
for line in reader:
    l = line
    val = l.rstrip("\n").split(" ")
    # print(val)
    array.append(val)
# print(array)

for count in range(len(array)):
    if "public" in array[count]:
        # print(count + 1)
        limit = len(array[count])
        # print(limit)
        for count2 in range(limit):
            # print(limit)
            # print(array[count])
            if array[count][count2] == "(":
                start = count2

                for count3 in range(limit):

                    if array[count][count3] == ")":
                        end = count3 + 1

                        for count4 in range(limit):
                            status = False
                            if array[count][count4] in keywords:
                                status = True
                                break

                        # print(status)
                        if status == False:
                            while start <= end:
                                print(array[count][start - 1], end=" ")
                                start += 1
                            print(" ")
