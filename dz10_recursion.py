def recursion(n):
    return step(0, n)


def step(i, n):
    if i > n:
        return 0
    elif i == n:
        return 1
    else:
        return step(i + 1, n) + step(i + 2, n) + step(i + 3, n)


if __name__ == "__main__":
    n = int(input("Enter the number of stairs: "))
    print("Ways to climb the stairs =", recursion(n))
