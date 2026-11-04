"""Assignment 4: N-Queens backtracking with a fixed first queen."""

# PRACTICAL TEST INPUT
# Run: python3 Assignment_4_N_Queens.py
# Type these responses at the prompts, pressing Enter after each:
#   Board size N: 4
#   Fixed queen row: 1
#   Fixed queen column: 2
# One valid board has queens at (row, column): (1,1), (2,3), (3,4), (4,2).


def solve_n_queens(n, first_row=1, first_column=1):
    """Return one solution, or None. Fixed row/column are 1-based."""
    if n <= 0:
        raise ValueError("Board size must be positive")
    if not (1 <= first_row <= n and 1 <= first_column <= n):
        raise ValueError("Fixed queen position must be inside the board")

    first_row -= 1
    first_column -= 1
    # queen_column[row] gives the queen's column, or -1 if not placed yet.
    queen_column = [-1] * n
    queen_column[first_row] = first_column

    def is_safe(row, column):
        for other_row, other_column in enumerate(queen_column):
            if other_column == -1 or other_row == row:
                continue
            same_column = other_column == column
            same_diagonal = abs(other_row - row) == abs(other_column - column)
            if same_column or same_diagonal:
                return False
        return True

    def place_queen(row):
        if row == n:
            return True
        if row == first_row:  # Keep the required queen fixed.
            return place_queen(row + 1)

        for column in range(n):
            if is_safe(row, column):
                queen_column[row] = column
                if place_queen(row + 1):
                    return True
                queen_column[row] = -1  # Undo this choice and try another.
        return False

    if place_queen(0):
        return queen_column
    return None


if __name__ == "__main__":
    n = int(input("Enter board size N: "))
    first_row = int(input("Fixed queen row (1-based, default 1): ") or "1")
    first_column = int(input("Fixed queen column (1-based, default 1): ") or "1")
    solution = solve_n_queens(n, first_row, first_column)

    if solution is None:
        print("No solution exists for that fixed queen position.")
    else:
        print("One valid board:")
        for queen in solution:
            print(" ".join("Q" if column == queen else "." for column in range(n)))
    print("Worst-case time: O(N!), with O(N) auxiliary space.")



"""
Theory to remember:
- N-Queens Problem: Place N queens on an N × N chessboard so that no two queens attack each other.
- Backtracking: Tries a solution and goes back if that solution is invalid.
- Recursion: Solves the problem by repeatedly calling the same function.
How to explain orally:

"I implemented the N-Queens problem using backtracking. I place queens row by row and check whether the position is safe. If no safe position is available, I remove the previous queen and try another position."

Three conditions to check:
1. No two queens in the same row.
2. No two queens in the same column.
3. No two queens on the same diagonal.
Example: N = 4, fixed queen at row 1, column 2.
. Q . .
. . . Q
Q . . .
. . Q .


Remember these terms:
- queen_column: Stores the column position of each queen.
- is_safe(): Checks whether a position is valid.
- place_queen(): Places queens recursively.
- -1: Indicates that no queen is placed in that row.
- Undo: Removes a queen when a solution fails.
Complexity:
- Time: O(N!) worst case.
- Space: O(N).

"""