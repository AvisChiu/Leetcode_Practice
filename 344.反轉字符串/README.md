思路
--
不能再簡單....     
快指針從前往後，慢指針從後往前。      
for 的次數為 List 長度的一半，結束...
```
pin2 = len(s) - 1
    
for i in range(len(s)/2):
    tmp = ""
    tmp = s[i] 
    s[i] = s[pin2]
    s[pin2] = tmp
    pin2 = pin2 - 1
```
