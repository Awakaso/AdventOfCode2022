
def read_input():
    file1 = open('Calories.txt', 'r')
    Lines = file1.readlines()

    calories = 0
    list_elfs = []

    for line in Lines:
        if line[:1] != '' and line[2:1].isnumeric():
            calories += int(line[:-1])
        else:
            list_elfs.append(calories)
            calories = 0

    calories = 0
    list_elfs.sort(reverse=True)
    for i in range(3):
        calories += list_elfs[i]

    print(calories)


if __name__ == '__main__':
    read_input()
