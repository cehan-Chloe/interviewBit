class Solution:
    # @param A : integer
    # @return a strings
    def convertToChar(self, n):
        return chr(ord('A') + n % 26)
    
    def convertToTitle(self, A):
        if A < 1:
            return None
        title = ''
        while A :
            A = A - 1
            pre = A % 26
            title += self.convertToChar(pre)
            A = A / 26
        return title[::-1]
            
