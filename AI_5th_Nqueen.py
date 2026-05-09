# ---------------- BACKTRACKING ---------------- #

backtracking_count = 0

def isSafe_Backtracking(board, row, col, n):

    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    i = row
    j = col

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i = row
    j = col

    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_Backtracking(board, row, n):

    global backtracking_count

    if row == n:
        backtracking_count += 1

        print(f"\nBacktracking Solution {backtracking_count}:\n")

        for i in range(n):
            for j in range(n):
                print(board[i][j], end=" ")
            print()

        return

    for col in range(n):

        if isSafe_Backtracking(board, row, col, n):

            board[row][col] = 1

            solve_Backtracking(board, row + 1, n)

            # Backtrack
            board[row][col] = 0


# ---------------- BRANCH AND BOUND ---------------- #

branch_bound_count = 0

def solve_BranchBound(board, row, n, columns, diag1, diag2):

    global branch_bound_count

    if row == n:
        branch_bound_count += 1

        print(f"\nBranch and Bound Solution {branch_bound_count}:\n")

        for i in range(n):
            for j in range(n):
                print(board[i][j], end=" ")
            print()

        return

    for col in range(n):

        # Bounding condition
        if columns[col] or diag1[row - col + n - 1] or diag2[row + col]:
            continue

        # Place queen
        board[row][col] = 1
        columns[col] = True
        diag1[row - col + n - 1] = True
        diag2[row + col] = True

        solve_BranchBound(board, row + 1, n, columns, diag1, diag2)

        # Backtrack
        board[row][col] = 0
        columns[col] = False
        diag1[row - col + n - 1] = False
        diag2[row + col] = False


# ---------------- MAIN FUNCTION ---------------- #

def main():

    n = int(input("Enter number of Queens: "))

    # -------- Backtracking -------- #
    print("\n========== USING BACKTRACKING ==========")

    board1 = [[0 for i in range(n)] for j in range(n)]

    solve_Backtracking(board1, 0, n)

    print("\nTotal Solutions using Backtracking =", backtracking_count)

    # -------- Branch and Bound -------- #
    print("\n========== USING BRANCH AND BOUND ==========")

    board2 = [[0 for i in range(n)] for j in range(n)]

    columns = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)

    solve_BranchBound(board2, 0, n, columns, diag1, diag2)

    print("\nTotal Solutions using Branch and Bound =", branch_bound_count)


if __name__ == "__main__":
    main()
