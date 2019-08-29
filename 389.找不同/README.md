思路
--
題目要求用哈希表，    
於是想到一個莫名其妙的辦法。
</br>
*邏輯*    
先把原始的 List 做成表格，key 是字母，value 是出現的次數。    
之後開始歷邊 t, 如果 t 裡面的字母有在 dictionary，則該 value 減 1，    
若不存在，則把新的字母的 value 變成 -1。    
因此最後只看 dictionary 裡面 value 為 -1 的那個 key 就是答案。
```
for i in s:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
```
```
for j in t:
    if j in dic:
        dic[j] -= 1
    else:
        dic[j] = -1
```
```
for items in t:
    if dic[items] == -1:
        return items
```
