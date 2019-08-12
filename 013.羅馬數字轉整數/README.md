思路：
--

構造字典 Dictionary
構造搜索邏輯
```
if s[i] in dic:
    list1.append(dic[s[i]])    
if i > 0:
    tmp = s[i-1] + s[i]
       if tmp in dic:
          list1.pop()
          list1.pop()
          list1.append(dic[tmp])
```
