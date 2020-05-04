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
# TO DO: Refactor code with this
#     x = (n-1)//3
#     y = (n-1)//5
#     z = (n-1)//15
#
#     sum_x = 3 * x * (1 + x)//2
#     sum_y = 5 * y * (1 + y)//2
#     sum_z = 15 * z * (1 + z)//2
#
#     return sum_x + sum_y - sum_z


def main():
    print(multiples_of3and5(sys.argv[1]))


if __name__ == "__main__":
    main()
