import sys
import math


def prime_summation(n):
    prime_list = [2]
    number = 3
    is_prime = True

    while number < n:
        for prime in prime_list:
            if prime > math.ceil(math.sqrt(number)):
                break
            if number % prime == 0:
                is_prime = False
                break

        if is_prime:
            prime_list.append(number)
        is_prime = True
        number += 2

    return sum(prime_list)


def main():
    print(prime_summation(sys.argv[1]))
    # print(prime_summation(17))
    # print(prime_summation(2001))
    # print(prime_summation(140759))
    # print(prime_summation(2000000))


if __name__ == "__main__":
    main()


