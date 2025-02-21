class Solution(object):
    def imageSmoother(self, img):
        m, n = len(img), len(img[0])
        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                neighbour = [img[x][y]
                             for x in (i-1, i, i+1)
                             for y in (j-1, j, j+1)
                             if 0 <= x < m and 0 <= y < n]
                result[i][j] = sum(neighbour) // len(neighbour)

        return result