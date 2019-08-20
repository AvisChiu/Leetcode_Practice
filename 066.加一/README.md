思路：
--
歷邊整個 digits ， 一個個抓出來組成一個完整的數字。    
```
tmp = 0
for i in range(len(digits)):
    s = digits[i]*(10**(len(digits)-i-1))
    tmp = tmp + s  
```
加一。
```
result = tmp + 1
```
</br>

轉成 String， 塞進一個 List 。
```
trans = str(result)
resList = []
for j in range(len(trans)):
    resList.append(trans[j])
```
