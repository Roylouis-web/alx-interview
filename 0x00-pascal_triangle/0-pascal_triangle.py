def factorial(n):
    """
        Computes the factorial of a number
    """

    if n <= 0:
        return 1
    return n * factorial(n - 1)


def binomial_sequence(a, b):
    """
        Computes the binomial sequence of
        the Pascal's Triangle
    """

    return factorial(a) // (factorial(a - b) * factorial(b))


def pascal_triangle(n):
    """
        Returns a list of list which is
        made up of sequences of the Pascal's Triangle
    """

    arr = []

    for i in range(n):
        temp = []
        for j in range(i + 1):
            temp.append(binomial_sequence(i, j))
        arr.append(temp)
    return arr
