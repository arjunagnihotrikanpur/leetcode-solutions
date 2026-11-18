class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:

        def solve(matrix):

            m = len(matrix)
            n = len(matrix[0])

            if m == 0 or n == 0:
                return []

            ret = []

            # Loop through first row
            x = 0
            for y in range(0, n):
                ret.append(matrix[x][y])

            # Loop through last column
            y = n-1
            for x in range(1, m):
                ret.append(matrix[x][y])

            # Loop through last row backwards
            if m > 1:
                x = m-1
                for y in range(n-2, -1, -1):
                    ret.append(matrix[x][y])

            # Loop through first column backwards
            if n > 1:
                y = 0
                for x in range(m-2, 0, -1):
                    ret.append(matrix[x][y])

            # Remove all Boundary Elements
            newMatrix = []

            for x in range(0, m):
                newRow = []

                for y in range(0, n):
                    if (x == 0 or y == 0 or x == m-1 or y == n-1):
                        pass
                    else:
                        newRow.append(matrix[x][y])

                if newRow:
                    newMatrix.append(newRow)

            if newMatrix:
                ret.extend(solve(newMatrix))

            return ret

        return solve(matrix)



        # I solved this medium problem by myself, first medium problem solved by myself.
        # Actually the first medium problem ever attempted
        # It took me 55 minutes exactly :)