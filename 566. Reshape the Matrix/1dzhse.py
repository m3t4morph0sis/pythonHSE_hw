class Solution:
    def matrixReshape(self, mat, r, c):
        rows = len(mat)
        cols = len(mat[0])
        if rows * cols != r * c:
            return mat
        nums = []
        for i in range(rows):
            for j in range(cols):
                nums.append(mat[i][j])
        result = []
        index = 0
        for i in range(r):
            new_row = []
            for j in range(c):
                new_row.append(nums[index])
                index += 1
            result.append(new_row)
        return result
if __name__ == "__main__":
    solution = Solution()
    mat = [[1, 2], [3, 4]]
    r = 1
    c = 4
    result = solution.matrixReshape(mat, r, c)
    print("исходная матрица:", mat)
    print("новый размер:", r, "x", c)
    print("результат:", result)
