"""Assignment 1: recursive and iterative Fibonacci implementations."""

# PRACTICAL TEST INPUT
# Run: python3 Assignment_1_Fibonacci.py
# When asked "Enter n", type: 10
# Expected result from both methods: 55 (F(0)=0, F(1)=1, ...).


def fibonacci_iterative(n):
    """Calculate F(n) with a loop. F(0)=0 and F(1)=1."""
    if n < 0:
        raise ValueError("n must be non-negative")

    previous, current = 0, 1
    for _ in range(n):
        previous, current = current, previous + current
    return previous


def fibonacci_recursive(n):
    """Direct textbook recursion (intentionally not optimized)."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


if __name__ == "__main__":
    number = int(input("Enter n to calculate F(n): "))
    if number > 35:
        print("The simple recursive method is very slow for n greater than about 35.")
    else:
        print("Iterative result:", fibonacci_iterative(number))
        print("Recursive result:", fibonacci_recursive(number))

    print("Iterative: O(n) time, O(1) extra space")
    print("Recursive: O(2^n) time, O(n) call-stack space")
