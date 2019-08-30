class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """  
        dic = {}
        licensePlate = str(licensePlate.lower())
        licensePlate = filter(str.isalpha, licensePlate)
        
        for i in licensePlate :
            if i in dic and i != ' ':
                dic[i] += 1
            if i not in dic and i != ' ':
                dic[i] = 1
        
        countzero = len(dic)
        
        new = []
        neww = []
        for j in words:
            dicc = dic.copy()
            for i in range(len(j)):
                if j[i] in dic and dicc[j[i]] != 0:
                    dicc[j[i]] -= 1
                # else: 
                #     dicc[j[i]] = 0
                    
            result = dicc.values().count(0)
            if result == countzero:
                if len(new) == 0:
                    new.append(j)
                elif len(j) < len(new[0]):
                    new.pop()
                    new.append(j)             
                    
        #==========================================
        
        
        if len(new) == 0:
            
            for j in words:
                dicc = dic.copy()
                
                for i in range(len(j)):
                    if j[i] in dic and dicc[j[i]] != 0:
                        dicc[j[i]] -= 1
                        
                result = sum(dicc.values())
                
                
                print(result)
                
                
                
                
                
                
                if len(neww) == 0:
                    neww.append(j)
                    neww.append(result)
                    
                if len(neww) != 0:
                    if result < neww[1]:
                        neww.pop()
                        neww.pop()
                        neww.append(j)
                        neww.append(result)
              
            
               
       
        if len(neww) != 0:
            return neww[0]
        else:
            return new[0]
        