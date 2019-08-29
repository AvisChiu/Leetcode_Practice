class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        # method 1: Dictionary 80.15%, 100%
        dic = {}
        for items in chars:
            if items in dic:
                dic[items] += 1       
            else:
                dic[items] = 1
        
        new = []
        for i in words:
            d = dic.copy()
            # print(d)
            new.append(i)
            for j in i:            
                if j in d and d[j] > 0:
                    d[j] = d[j] - 1
                else: 
                    new.remove(i)
                    break
                
        count = 0
        for i in new:
            count = count + len(i)
        
        # print(dic)
        # print(new)
        return count
        