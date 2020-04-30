import sys


def nth_prime(n):
    prime = [2]
    number = 2

    while len(prime) < n:
        for index, nums in enumerate(prime):
            if number % nums == 0:
                number += 1
                break
            else:
                if index == len(prime) - 1:
                    prime.append(number)

    return prime[-1]


def main():
    print(nth_prime(sys.argv[1]))
    # print(nth_prime(6))
    # print(nth_prime(10))
    # print(nth_prime(100))
    # print(nth_prime(1000))
    # print(nth_prime(10001))


if __name__ == "__main__":
    main()


