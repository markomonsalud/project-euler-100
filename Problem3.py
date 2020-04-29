import sys


def largest_prime_factor(number):
    largest_prime = 0
    prime = 2
    number = int(number)

    while prime <= number:
        if number % prime == 0:
            largest_prime = prime
            number = number/prime
        else:
            prime = prime + 1

    return largest_prime


def main():
    print(largest_prime_factor(sys.argv[1]))


if __name__ == "__main__":
    main()
