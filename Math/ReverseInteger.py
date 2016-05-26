class Solution:
    # @param A : integer
    # @return an integer
    def reversePositive(self, n):
        reverseInt = 0
        while n:
            reverseInt = reverseInt * 10 + n % 10
            n /= 10
        return reverseInt
    
    def reverse(self, A):
        # if abs(A) >  2147483647:
        #     return 0
        if A > 0:
            reverseInt = self.reversePositive(A)
        else:
            reverseInt = -1 * self.reversePositive(abs(A))
        if abs(reverseInt) >  2147483647:
            return 0
        else:
            return reverseInt
