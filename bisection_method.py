"""Module implementing the bisection method to find square roots."""
def square_root_bisection(number, tolerance=1e-7, max_iterations=1000):
    """Approximate the square root of a non-negative number using the bisection method."""
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number

    left = 0.0
    right = number if number >= 1 else 1.0

    for _ in range(max_iterations):
        mid = (left + right) / 2.0
        square = mid * mid

        # Stop when interval width guarantees root is within `tolerance`
        if (right - left) / 2.0 <= tolerance:
            print(f"The square root of {number} is approximately {mid}")
            return mid

        # Narrow the interval based on whether mid^2 is below or above the target
        if square < number:
            left = mid
        else:
            right = mid

    print(f"Failed to converge within {max_iterations} iterations")
    return None


print(square_root_bisection(0.001, 1e-7, 50))
print(square_root_bisection(0.25, 1e-7, 50))
print(square_root_bisection(81, 1e-3, 50))
print(square_root_bisection(225, 1e-3, 100))
print(square_root_bisection(225, 1e-7, 10))
