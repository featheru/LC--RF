class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        62% for memory
        62% for runtime
        """
        idx_start = 0
        idx_end = len(matrix)-1

        while idx_start < len(matrix)/2:
            shift = idx_end - idx_start
            row = idx_start
            col = idx_start*1
            for i in range(shift):
                curr_value = matrix[row][col]
                new_row = row
                new_col = col
                shift_c = (idx_end - idx_start - col + idx_start)
                shift_r = (idx_end - idx_start - shift_c)
                moves = [[shift_r, shift_c], [shift_c, -1*shift_r], [-1*shift_r, -1*shift_c], [-1*shift_c, shift_r]]
                for move in moves:
                    new_row = new_row + move[0]
                    new_col = new_col + move[1]
                    tmp_value = matrix[new_row][new_col]
                    matrix[new_row][new_col] = curr_value
                    curr_value = tmp_value
                col += 1
                shift -= 1

            idx_start += 1
            idx_end -= 1


matrix_even = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
matrix_odd = [[1,2,3],[4,5,6],[7,8,9]]

Solution().rotate(matrix_odd)
for item in matrix_odd:
    print(item)
print(matrix_even == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])