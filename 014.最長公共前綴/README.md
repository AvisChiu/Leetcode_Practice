思路：
--

如果題目變成比較數字的公共前綴，很自然地會想到拿最長的和最短的去比較。   
針對 String 來說，同樣地可以想辦法把這兩個字符找出來。   
利用ASCII的編碼機制，找到最大和最小的字符。（與字符的長短有關）
```
a = min(strs)
b = max(strs)
```
原理
```
 a < b, ab < ac , ab < abc
```
下一步，獲得關於這兩個字符各個字元的ASCII的編碼，並塞入 list
```
for i in range(len(a)):
    list1.append(ord(a[i]))
for i in range(len(b)):
    list2.append(ord(b[i]))
```
最後制定搜索邏輯: 想法是逐位比較，相同則新增到 list，發現有不一樣的，立刻跳出。
```
for i in range(c):
    if a[i] == b[i]:
        list3.append(a[i])
    else:
        break
```
*Note

因為是最長前綴，以下情況不需要考慮。
```
["flow","aafl"]
```
