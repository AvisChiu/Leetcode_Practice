 		
class Solution(object):
    def isValid(self, s):
        
        dic = {}
        dic["("] = 1
        dic[")"] = -1
        dic["["] = 2
        dic["]"] = -2
        dic["{"] = 3
        dic["}"] = -3
        
        re=[]
        if s=='':
            return True
        else:
            re.append(dic[s[0]])
            
        if sum(re)<0:
            return False
        
        # re: ['(']
        
        
        for i in s[1:]:
            if re==[]:
                re.append(dic[i])
            elif dic[i]+re[-1]==0:
                re.pop()
            else:
               
                re.append(dic[i])
        return re==[]





'''
 		a = '()'
        b = '{}'
        c = '[]'
        
        while a in s or b in s or c in s:
            
            s = s.replace(a,'')
            s = s.replace(b,'')
            s = s.replace(b,'')

'''