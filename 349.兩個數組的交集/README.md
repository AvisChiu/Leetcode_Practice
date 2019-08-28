思路
--

題目不要求輸出的順序，這樣就真的簡單到不行...
```
newList = []
for i in nums1:
    if i in nums2:
        if i not in newList:
            newList.append(i)
return newList
```
拿一個 List 的元素，一個個去跟另一個裡面的去比對。    
有的話，塞進一個新的 List，而且不要重複塞。

*方法二*    
set 的操作
