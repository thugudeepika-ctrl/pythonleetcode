class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Special case: if only one row or shorter than numRows
        if numRows == 1 or numRows >= len(s):
            return s

        # Create a list for each row
        rows = [''] * numRows
        cur_row, going_down = 0, False

        # Build the zigzag pattern
        for c in s:
            rows[cur_row] += c
            # Change direction at the first or last row
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            # Move up or down
            cur_row += 1 if going_down else -1

        # Combine all rows
        return ''.join(rows)

        