

def read_input():
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()

    priority_sum = 0

    for line in Lines:
        str_line = line[:-1]
        pos_mid = round(len(str_line) / 2)

        for i in str_line[:pos_mid]:
            if i in str_line[pos_mid:]:
                if i.isupper():
                    priority_sum += (ord(i) + 26 - 64)
                    break
                else:
                    priority_sum += (ord(i) - 96)
                    break

    print(priority_sum)


if __name__ == '__main__':
    read_input()