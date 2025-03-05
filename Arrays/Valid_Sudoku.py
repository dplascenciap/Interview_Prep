"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without
repetition.

Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

def is_valid_sudoku(board):
    # Arrays to track occurrences of digits (1-9)
    rows = [[False] * 9 for _ in range(9)]  # Tracks digits in each row
    cols = [[False] * 9 for _ in range(9)]  # Tracks digits in each column
    boxes = [[False] * 9 for _ in range(9)] # Tracks digits in each 3x3 box

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue  # Skip empty cells

            num = int(board[r][c]) - 1  # Convert '1'-'9' to index 0-8
            box_index = (r // 3) * 3 + (c // 3)  # Find sub-box index

            # Check if the number already exists in row, column, or box
            if rows[r][num] or cols[c][num] or boxes[box_index][num]:
                return False  # Invalid Sudoku

            # Mark number as seen in row, column, and box
            rows[r][num] = cols[c][num] = boxes[box_index][num] = True

    return True

def is_valid_sudoku_set(board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sub_boxes = [set() for _ in range(9)]

        # Scan the grid
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    continue

                # Calculate sub-box index
                sub_index = (r // 3) * 3 + (c // 3)

                # Check for duplicates
                if value in rows[r] or value in cols[c] or value in sub_boxes[sub_index]:
                    return False

                # Add value to set
                rows[r].add(value)
                cols[c].add(value)
                sub_boxes[sub_index].add(value)

        return True

def is_valid_sudoku_dict(board):
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True

def test_is_valid_sudoku():
    # Valid Sudoku Board
    valid_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    assert is_valid_sudoku(valid_board) == True, "Test Case 1 Failed: Should return True"

    # Invalid Board (Row conflict: two '5's in the first row)
    invalid_row = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "5"],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    assert is_valid_sudoku(invalid_row) == False, "Test Case 2 Failed: Row conflict"

    # Invalid Board (Column conflict: two '3's in the first column)
    invalid_column = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        ["5", "9", "8", ".", ".", ".", ".", "6", "."],  # '5' repeats in column 1
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    assert is_valid_sudoku(invalid_column) == False, "Test Case 3 Failed: Column conflict"

    # Invalid Board (Sub-box conflict: two '9's in the top-left 3x3 box)
    invalid_subbox = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        ["9", "9", "8", ".", ".", ".", ".", "6", "."],  # Two '9's in the same 3x3 box
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    assert is_valid_sudoku(invalid_subbox) == False, "Test Case 4 Failed: Sub-box conflict"

    # Edge Case: Empty Board (Should be valid)
    empty_board = [["."] * 9 for _ in range(9)]
    assert is_valid_sudoku(empty_board) == True, "Test Case 5 Failed: Empty board should be valid"

    print("All test cases passed!")

# Run the tests
test_is_valid_sudoku()