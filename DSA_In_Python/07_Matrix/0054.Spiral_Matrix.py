class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        ROW, COL = len(matrix), len(matrix[0])
        T, R, B, L = 0, COL-1, ROW-1, 0
        spiral = []

        while L <= R and T <= B:
            if L <= R:
                [spiral.append(matrix[T][i]) for i in range(L, R+1)]
                T += 1
            if T <= B:
                [spiral.append(matrix[i][R]) for i in range(T, B+1)]
                R -= 1
            if L <= R and T <= B:
                [spiral.append(matrix[B][i]) for i in range(R, L-1, -1)]
                B -= 1
            if T <= B and L <= R:
                [spiral.append(matrix[i][L]) for i in range(B, T-1, -1)]
                L += 1
        return spiral

print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
