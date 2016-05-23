class Solution:
    # @param A : integer
    # @return a list of integers
    def isPrime(self, A):
        for i in range(2,int(A**0.5+1)):
            if A % i == 0:
                return 0
        return 1
    
    def sieve(self, A):
        if A <= 1:
            return None
        if A == 2:
            return [2]
        result = []
        for i in range(2,A+1):
            res = self.isPrime(i)
            if res == 1:
                result.append(i)
        return result        
        
