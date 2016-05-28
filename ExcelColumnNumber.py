class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        columnNum = 0
        while len(A) > 0:
            columnNum = columnNum * 26 + ord(A[0]) - ord('A') + 1
            A = A[1:]
        return columnNum
