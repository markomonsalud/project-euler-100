import sys
import math


def nth_prime(n):
    prime = [2]
    number = 3
    is_prime = True

    while len(prime) < n:
        for nums in prime:
            if nums > math.ceil(math.sqrt(number)):
                break
            if number % nums == 0:
                is_prime = False
                break

        if is_prime:
            prime.append(number)
        is_prime = True

        number += 2

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


