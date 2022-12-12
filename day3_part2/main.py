priority_sum = 0
badge_list = []


def read_input():
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()

    return Lines


def sumCalc(Lines, priority_sum):
    str_line1 = ''
    str_line2 = ''
    str_line3 = ''
    num = 1

    for line in Lines:
        if num == 1:
            str_line1 = line
        elif num == 2:
            str_line2 = line
        elif num == 3:
            str_line3 = line

        num += 1

        if num == 4:
            Lines = Lines[3:]
            break

    for item in str_line1[:-1]:
        if item in str_line2[:-1] and item in str_line3[:-1]:
            if item.isupper():
                priority_sum += (ord(item) + 26 - 64)
                break
            else:
                priority_sum += (ord(item) - 96)
                break

    if Lines:
        sumCalc(Lines, priority_sum)
    else:
        print(priority_sum)


if __name__ == '__main__':
    Lines = read_input()
    sumCalc(Lines, priority_sum)
