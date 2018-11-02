def test(num):
    lists = [1, 2, 5, 10]
    number = 0
    for one in lists[::-1]:
        if num >= one:
            number += num // one
            num = num % one
        if num == 0:
            print(number)
            return number


if __name__ == '__main__':
    test(7)
