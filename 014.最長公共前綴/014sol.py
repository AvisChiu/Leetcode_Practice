class Solution(object):
    def longestCommonPrefix(self, strs):
    
        if len(strs) == 0:
            return ""
    
        else:   
            a = min(strs)
            b = max(strs)

            list1 = []
            list2 = []

            for i in range(len(a)):
                list1.append(ord(a[i]))
            for i in range(len(b)):
                list2.append(ord(b[i]))

            c = min(len(a),len(b))
        
       
    
            list3 = []
            result=""
            for i in range(c):
                if a[i] == b[i]:
                    list3.append(a[i])
                else:
                    break

            return result.join(list3)