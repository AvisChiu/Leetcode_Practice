思路
--
算是沒有什麼技巧一步一步來的題目。    
先把 chars 裡面的東西做成 Dictionary，key 為字母，value 為次數，這很常規。     
```
for items in chars:
    if items in dic:
        dic[items] += 1       
    else:
        dic[items] = 1
```
接著構造一個邏輯：    
即歷邊 words 裡面的單詞，且歷邊單詞的每一個字母。    
邏輯就是每經過一個字母，dictionary 裡面對應的次數就減 1，    
如果次數少於 0 ，則說明沒有辦法構造這個單詞。  
```
new = []
for i in words:
    d = dic.copy()
    # print(d)
    new.append(i)
    for j in i:            
        if j in d and d[j] > 0:
            d[j] = d[j] - 1
        else: 
            new.remove(i)
            break
```
中間有用到一個 List 去存符合要求的單詞。（先存下來，不符合再刪掉）
</br>
Note
--
需要注意 dictionary 的用法，每次進入 for 都要初始一份 dictionary。   
```
d = dic // 錯誤：會更改到原始的 dictionary
d = dic.copy() // 正確作法
```
