def multiplication_table():
    table = [[0] * 12 for _ in range(12)]

    for i in range(1, 13):
        for j in range(1, 13):
            table[i - 1][j - 1] = i * j

    for row in table:
        print(" ".join(str(n).rjust(4) for n in row))

multiplication_table()
#Count around the perimeter of a square matrix:
def count_around(start_num, matrix_size):
    matrix = [[0] * matrix_size for _ in range(matrix_size)]
    num = start_num

    for i in range(matrix_size):
        matrix[0][i] = num
        num += 1

    for i in range(1, matrix_size):
        matrix[i][-1] = num
        num += 1

    for i in range(matrix_size - 2, -1, -1):
        matrix[-1][i] = num
        num += 1

    for i in range(matrix_size - 2, 0, -1):
        matrix[i][0] = num
        num += 1

    for row in matrix:
        print(" ".join(str(n).rjust(4) for n in row))

count_around(5, 5)

def is_prime(num):
    """Returns True if the given number is prime, False otherwise."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True



def count_primes(start, end):
    """Returns the count of prime numbers between start and end (inclusive)."""
    count = 0
    for num in range(start, end + 1):
        if is_prime(num):
            count += 1
    print(count)

count_primes(1, 100)