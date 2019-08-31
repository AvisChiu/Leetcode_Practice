class Solution(object):
    def uncommonFromSentences(self, A, B):
       
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A = A.split()
        B = B.split()
        
        dicA = {}
        result = []
        
        
        for i in A:
            if i in dicA:
                dicA[i] += 1
            else:
                dicA[i] = 1
                
        for i in B:
            if i in dicA:
                dicA[i] += 1
            else:
                dicA[i] = 1
                
        for key, value in dicA.items():
            if value == 1:
                result.append(key)
        
        return result
        
        
        