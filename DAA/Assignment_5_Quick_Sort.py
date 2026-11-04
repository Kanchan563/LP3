"""Assignment 5: deterministic and randomized quicksort."""

# PRACTICAL TEST INPUT
# Run: python3 Assignment_5_Quick_Sort.py
# At the prompt, type: 8 3 5 1 9 2
# Both algorithms should print the sorted list: [1, 2, 3, 5, 8, 9].

import random


def quicksort_deterministic(values):
    """Sort in place, always selecting the last element as pivot."""
    def sort(low, high):
        if low >= high:
            return

        pivot = values[high]
        smaller_end = low - 1
        for current in range(low, high):
            if values[current] <= pivot:
                smaller_end += 1
                values[smaller_end], values[current] = values[current], values[smaller_end]

        pivot_position = smaller_end + 1
        values[pivot_position], values[high] = values[high], values[pivot_position]
        sort(low, pivot_position - 1)
        sort(pivot_position + 1, high)

    sort(0, len(values) - 1)
    return values


def quicksort_randomized(values):
    """Sort in place, choosing a random pivot for each partition."""
    def sort(low, high):
        if low >= high:
            return

        random_pivot = random.randint(low, high)
        values[random_pivot], values[high] = values[high], values[random_pivot]
        pivot = values[high]

        smaller_end = low - 1
        for current in range(low, high):
            if values[current] <= pivot:
                smaller_end += 1
                values[smaller_end], values[current] = values[current], values[smaller_end]

        pivot_position = smaller_end + 1
        values[pivot_position], values[high] = values[high], values[pivot_position]
        sort(low, pivot_position - 1)
        sort(pivot_position + 1, high)

    sort(0, len(values) - 1)
    return values


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Deterministic quicksort:", quicksort_deterministic(numbers.copy()))
    print("Randomized quicksort:   ", quicksort_randomized(numbers.copy()))
    print("Both average O(n log n), worst-case O(n^2); quicksort is not stable.")
    print("Average recursion space is O(log n); worst-case recursion space is O(n).")



"""
Theory to remember:
- Quick Sort: A sorting algorithm that divides an array using a pivot.
- Divide and Conquer: Divides a problem into smaller subproblems, solves them, and combines the results.
- Pivot: An element used to partition the array.
- Partitioning: Arranges smaller elements before the pivot and larger elements after it.
How to explain orally:

"I implemented two types of Quick Sort. Deterministic Quick Sort always selects the last element as pivot, while Randomized Quick Sort selects a random pivot. Both use partitioning and recursion to sort the array."

Difference:
Deterministic	Randomized
Last element as pivot	Random element as pivot
Fixed selection	Random selection
Depends more on input order	Reduces chance of consistently poor partitions

Example:

Input: [8, 3, 5, 1, 9, 2]

Output: [1, 2, 3, 5, 8, 9]

Remember these terms:
- random.randint(): Selects a random pivot index.
- smaller_end: Tracks smaller elements.
- low >= high: Base condition.
- In-place sorting: Modifies the original array.
Complexity:
Case	Time
Best	O(n log n)
Average	O(n log n)
Worst	O(n²)

Space: Average O(log n), worst O(n).

"""