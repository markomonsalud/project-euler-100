import sys


def sum_square_difference(n):
    total = 0
    for i in range(1, n + 1):
        for j in range(i+1, n + 1):
            total += 2*i*j

    return total


def main():
    print(sum_square_difference(sys.argv[1]))


if __name__ == "__main__":
    main()
