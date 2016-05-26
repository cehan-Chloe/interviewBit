class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        while B != 0:
            (A, B) = (B, A % B)
        return A
            
