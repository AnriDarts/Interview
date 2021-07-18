# reverse entire string and check if it matches the original one
def palindromeDetectorEasy(name):
    if name == name[::-1]:
        # print(name + "is palindrome")
        return True
    else:
        # print(name + "isn't  palindrome")
        return False


# go trough each character of a string and check if strings positive index char = strings negative index char
def palindromeDetectorHardWay(name):
    for i in range(len(name)):
        if name[i] == name[-1]:
            # print(name + "is palindrome")
            return True
        else:
            # print(name + "isn't  palindrome")
            return False


def coinCounter(n):
    coin_count = 0

    if n % 10 > 5:
        n -= 5
        coin_count += 1
    else:
        while n % 10 != 0:
            n -= 1
            coin_count += 1

    while n > 49:
        n -= 50
        coin_count += 1

    while n > 19:
        n -= 20
        coin_count += 1

    if n != 0:
        n -= 10
        coin_count += 1

    return coin_count


def CheckParentheses(inp):

    if len(inp) % 2 == 0:
        for i in range(len(inp) // 2):
            if inp[i] != inp[-i - 1]:
                # print("true")
                return True
            else:
                # print("false")
                return False
    else:
        # print("false2")
        return False


# find number of ways to representing a number as a sum of 1's and 2's

# Function to multiply matrix.
def multiply(F, M):
    x = F[0][0] * M[0][0] + F[0][1] * M[1][0]
    y = F[0][0] * M[0][1] + F[0][1] * M[1][1]
    z = F[1][0] * M[0][0] + F[1][1] * M[1][0]
    w = F[1][0] * M[0][1] + F[1][1] * M[1][1]

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w


# Power function in log n
def power(F, n):
    if n == 0 or n == 1:
        return
    M = [[1, 1], [1, 0]]

    power(F, n // 2)
    multiply(F, F)

    if n % 2 != 0:
        multiply(F, M)


# /* function that returns (n+1)th Fibonacci number
# Or number of ways to represent n as sum of 1's
# 2's */
def countWays(n):
    F = [[1, 1], [1, 0]]
    if n == 0:
        return 0
    power(F, n)

    return F[0][0]


# Driver Code
steps = 4
print(countWays(steps))