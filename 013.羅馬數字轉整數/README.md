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
解釋：
--
對字串的每一位，都把對應的數字 append 到 list 裡面。   
其次，從 i = 1 開始，
```
s[i-1] + s[i]
```
代表當前字元與上一位的字元的組合，此時 list 已經新增了 2 次數字。   
若組合在字典裡面存在，則刪除剛剛新增的數字， 故要 pop 2次。
