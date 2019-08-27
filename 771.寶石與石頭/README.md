思路
--
題目要求用哈希表，題目本身也非常簡單。
```
dic = {}
for items in J:
    dic[items] = 1
```
```
count = 0
for i in range(len(S)):
    if S[i] in dic:
    count = count + 1
                
return count
```
其實不建立 dictionary 也可以，見了就消耗了 O(n)的時間複雜度。    
邏輯就是歷邊 S 裡面的元素，一個個去對，判斷有沒有在 dictionary，有的話 counter 加 1.
