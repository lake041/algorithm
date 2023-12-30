def find(num):
    if not num % 2:
        return num + 1

    num_bin = list(map(int, "0" + format(num, 'b')))
    index = -1
    while True:
        index -= 1
        if not num_bin[index]:
            num_bin[index] = 1
            num_bin[index+1] = 0
            break
    return int(''.join(list(map(str, num_bin))), 2)


def solution(numbers):
    return [find(number) for number in numbers]