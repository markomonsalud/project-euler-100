import sys


def multiples_of3and5(number):
    total = 0
    for num in range(1, int(number)):
        if num % 3 == 0:
            total += num
        if num % 5 == 0:
            total += num
        if num % 15 == 0:
            total -= num
    return total


def main():
    print(multiples_of3and5(sys.argv[1]))


if __name__ == "__main__":
    main()
