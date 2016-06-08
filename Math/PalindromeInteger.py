class Solution:
    # @param A : integer
    # @return a boolean value ( True / False )
    def isPalindrome(self, A):
        # convert int to string
        # the step is -1, then reverse the string. 
        # if they are the same, the integer is Palindrome Integer
        A = str(A)
        return A == A[::-1]        
