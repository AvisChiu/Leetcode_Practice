class Solution(object):
    
    def romanToInt(self, s):
        
        
        str = ""
        list1 = []
        dic = {}
        dic["I"] = 1
        dic["V"] = 5
        dic["X"] = 10
        dic["L"] = 50
        dic["C"] = 100
        dic["D"] = 500
        dic["M"] = 1000
        dic["IV"] = 4
        dic["IX"] = 9
        dic["XL"] = 40
        dic["XC"] = 90
        dic["CD"] = 400
        dic["CM"] = 900
        
        if s in dic:
            return (dic[s])
        
        else:
            for i in range(len(s)):
                
                if s[i] in dic:
                    list1.append(dic[s[i]])
                    
                if i > 0:
                    tmp = s[i-1] + s[i]
                
                    if tmp in dic:
                        list1.pop()
                        list1.pop()
                        list1.append(dic[tmp])
                    
                
        result = sum(list1)
        return result