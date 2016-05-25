class Solution:
    # @param A : integer
    # @return a strings
    def list2int(self,numList):
        # join method is applied to string, so use map to change int in numList to str
	s = ''.join(map(str, numList))
        return int(s)
    
    def findDigitsInBinary(self, A):
        result_list = []
        if A == 0:
            return 0
        while A != 0:
            quo = A / 2
            reminder = A % 2 
            result_list.insert(0, reminder)
            A = quo
        result_list = self.list2int(result_list)
        return result_list
