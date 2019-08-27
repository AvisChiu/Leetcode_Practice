class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        # method 1: sort

        A.sort()
        result = 0
        for i in range(len(A)):
            if A[i] == A[i+1]:
                result = A[i]
                break
        return result
    
    
    
        # method 2: dictionary
        dic = {}
        for i in A:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        count = len(A) // 2
        for key, value in dic.items():
            if value == count:
                return key