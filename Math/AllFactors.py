class Solution:
#     # @param A : integer
#     # @return a list of integers
#     the first method exceed time limit
#     def allFactors(self, A):
#         result = [1]
#         if A <= 1:
#             return result;
#         result.append(A)
#         i = 2
#         while i <= math.sqrt(A):
#             if A % i == 0:
#                 result.append(i)
#                 if i is not math.sqrt(A):
#                     result.append(A/i)
#             i += 1
#         result.sort()
#         return result
    def allFactors(self, A):
        firstHalf = []
        secondHalf = []
        for i in range(1, int(A ** 0.5) + 1) :
            if A%i == 0 :
                firstHalf.append(i)
                if i != A ** 0.5 :
                    secondHalf.insert(0, A/i)
        firstHalf.extend(secondHalf)
        return firstHalf
    
    
    
