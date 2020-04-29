import sys


def fib_even_sum(number):
    total = 0
    fib_number = 0
    prev_fib_number = 1
    second_prev_fib_number = 0
    while fib_number <= int(number):
        if fib_number % 2 == 0:
            total += fib_number

        fib_number = prev_fib_number + second_prev_fib_number
        second_prev_fib_number = prev_fib_number
        prev_fib_number = fib_number

    return total


def main():
    print(fib_even_sum(sys.argv[1]))


if __name__ == "__main__":
    main()
