import sys
import math


def special_pythagorean_triplet(n):
    sum_of_abc = int(n)
    for a in range(1, sum_of_abc):
        for b in range(a+1, sum_of_abc):
            c = math.sqrt(a ** 2 + b ** 2)
            if a+b+c == sum_of_abc:
                return int(a*b*c)


def main():
    print(special_pythagorean_triplet(sys.argv[1]))
    # print(special_pythagorean_triplet(24))
    # print(special_pythagorean_triplet(120))
    # print(special_pythagorean_triplet(1000))


if __name__ == "__main__":
    main()
