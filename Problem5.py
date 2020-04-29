import sys


def smallest_multiple(n):
    multiple = 1
    n = int(n)
    for i in range(2, n+1):
        multiple = least_common_multiple(multiple, i)
    return int(multiple)


def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)


def least_common_multiple(a, b):
    return a * b / greatest_common_divisor(a, b)


def main():
    print(smallest_multiple(sys.argv[1]))


if __name__ == "__main__":
    main()
