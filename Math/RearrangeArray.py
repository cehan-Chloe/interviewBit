class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        if A is None:
            return A
        l = len(A)
        for i in range(0,l):
            A[i] = A[i] + A[A[i] % l]% l *l
        # map(lambda x:x / 10, A)
        for i in range(0,l):
            A[i] /= l
        return A
        
