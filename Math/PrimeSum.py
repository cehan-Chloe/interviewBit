class Solution:
    # @param A : integer
    # @return a list of integers
    
    # this method have memory limit exceeded problem at first
    # because i use range other than xrange in primesum function
    def isPrime(self, A):
        if A < 2:
            return 1
        for i in range(2, int(A**0.5+1)):
            if A % i == 0:
                return 0
        return 1
    
    def primesum(self, A):
        for i in xrange(2, A):
            if self.isPrime(i) and self.isPrime(A - i):
                    return i,A-i
