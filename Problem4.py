import sys


def largest_palindrome(n):
    n = int(n)
    palindrome_list = []
    for i in range((10 ** n) - 1, 1, -1):
        for j in range((10 ** n) - 1, 1, -1):
            palindrome = i * j
            palindrome_string = str(palindrome)

            if palindrome_string == palindrome_string[::-1]:
                palindrome_list.append(palindrome)

    return max(palindrome_list)


def main():
    print(largest_palindrome(sys.argv[1]))


if __name__ == "__main__":
    main()
