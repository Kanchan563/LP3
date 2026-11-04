"""Assignment 3: 0/1 knapsack using bottom-up dynamic programming."""

# PRACTICAL TEST INPUT
# Run: python3 Assignment_3_01_Knapsack.py
# No typing is needed; the PDF example is already set below:
# weights = [3, 4, 6, 5], profits = [2, 3, 1, 4], capacity = 8
# Expected maximum profit: 6, by selecting items 1 and 4.


def knapsack_01(weights, profits, capacity):
    """Return the best profit, selected 1-based item numbers, and DP table."""
    if len(weights) != len(profits):
        raise ValueError("Give one profit for every item weight")
    if capacity < 0 or any(weight < 0 for weight in weights):
        raise ValueError("Weights and capacity must be non-negative")

    item_count = len(weights)
    # dp[i][c] is the best profit using the first i items and capacity c.
    dp = [[0] * (capacity + 1) for _ in range(item_count + 1)]

    for i in range(1, item_count + 1):
        weight = weights[i - 1]
        profit = profits[i - 1]
        for current_capacity in range(capacity + 1):
            # First consider leaving this item out.
            dp[i][current_capacity] = dp[i - 1][current_capacity]

            # If it fits, compare that with taking the whole item.
            if weight <= current_capacity:
                take = profit + dp[i - 1][current_capacity - weight]
                dp[i][current_capacity] = max(dp[i][current_capacity], take)

    chosen_items = []
    current_capacity = capacity
    for i in range(item_count, 0, -1):
        if dp[i][current_capacity] != dp[i - 1][current_capacity]:
            chosen_items.append(i)  # Items are numbered starting from 1.
            current_capacity -= weights[i - 1]
    chosen_items.reverse()

    return dp[item_count][capacity], chosen_items, dp


if __name__ == "__main__":
    # Values from the assignment question.
    weights = [3, 4, 6, 5]
    profits = [2, 3, 1, 4]
    capacity = 8

    best_profit, chosen, table = knapsack_01(weights, profits, capacity)
    print("Weights:", weights)
    print("Profits:", profits)
    print("Capacity:", capacity)
    print("Maximum profit:", best_profit)
    print("Selected item numbers:", chosen or "none")
    print("DP table (rows are item counts, columns are capacities):")
    for row in table:
        print(" ".join(f"{value:2}" for value in row))
    print("Complexity: O(nC) time and O(nC) space, where C is capacity.")



"""
Theory to remember:
- Knapsack Problem: Select items to get maximum profit without exceeding the given capacity.
- Dynamic Programming (DP): Solves a problem by storing results of smaller subproblems to avoid repeated calculations.
- 0/1 Knapsack: Each item can either be selected once or not selected.
- Bottom-Up Approach: Solves smaller problems first and builds towards the final answer.
How to explain orally:

"I implemented the 0/1 Knapsack problem using a DP table. For every item, I check whether including it gives more profit than excluding it. Finally, I find the maximum profit and selected items."

Example:
- Weights = [3, 4, 6, 5]
- Profits = [2, 3, 1, 4]
- Capacity = 8
Final result
6
Maximum profit

Selected items: 1 and 4 (total weight = 8)

Remember these terms:
- dp[i][c]: Maximum profit using first i items with capacity c.
- max(): Selects the maximum profit.
- Backtracking: Finds which items were selected.
Complexity:
- Time: O(n × C)
- Space: O(n × C)

"""