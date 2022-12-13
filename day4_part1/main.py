

def read_input():
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()

    counter = 0

    for line in Lines:
        splited_line = line.split(',')

        range1 = splited_line[0]
        range2 = splited_line[1].strip('\n')

        if range1 == range2:
            counter += 1
        else:
            range1_values = range1.split('-')
            range2_values = range2.split('-')

            if int(range1_values[0]) <= int(range2_values[0]) and int(range1_values[1]) >= int(range2_values[1]):
                counter += 1
            elif int(range1_values[0]) >= int(range2_values[0]) and int(range1_values[1]) <= int(range2_values[1]):
                counter += 1

    print(counter)


if __name__ == '__main__':
    read_input()
