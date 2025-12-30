"""Fibonacci number calculator using dynamic programming."""
def fibonacci(n):
    """Function to calculate the nth Fibonacci number using dynamic programming."""
    sequence = [0, 1]

    # Handle base cases
    if n < 2:
        return sequence[n]

    # Dynamic programming
    for i in range(2, n + 1):
        sequence.append(sequence[i - 1] + sequence[i - 2])

    return sequence[n]

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(5))
print(fibonacci(10))
print(fibonacci(15))
