class Solution:
    # @param A : integer
    # @return a boolean
    def isPower(self, A):
        if A is 1:
            return 1
        for i in range(2,int(A**0.5)+1):
            num = A
            while num % i is 0:
                num = num / i
            if num == 1:
                return 1
        return 0
