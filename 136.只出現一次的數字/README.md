思路：
--

*方法一：List*
歷邊 List，每經歷一個，把它 append 到新的 List。   
*邏輯*
若新的 list 已經有了，則把這個元素再新的 list 裡面移除。
這部分的時間複雜度是 O(n) , 因為在找有沒有的時候是從頭開始找。
```
empty_ = []
for items in nums:
    if items not in empty_:
        empty_.append(items)
    else:
        empty_.remove(items)
```
但是題目要求用 Hash Table，自然想到用 Dictionary。   

*方法一：Dictionary*
邏輯跟上面一樣...
```
for items in nums:
    try:
        dic.pop(items)
    except:
        dic[items] = 1
```
意思就是先把所有的元素當成 key，然後 value 都等於 1。   
例如：
```
1 2 3 4 1 2 3 
```
一開始從 1～4 dictionary 都開始走 except 的部分。    
到了 4 之後， dictionary 開始進行清楚動作， 走 pop 的部分。   
這個方法雖然節省了時間複雜度，但是增加了空間複雜度。

Note: 題目說明重複的元素只有兩次，若重複三次就GG
--
