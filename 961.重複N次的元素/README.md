思路
--
個人覺得仔細想一下其實不需要用到 Dictionary。    
把 List 從小到大排，接著歷邊（N/2次，一開始每想到），     
判斷條件就是如下，
```
if A[i] == A[i+1]
```
```
A.sort()
result = 0
for i in range(len(A)):
    if A[i] == A[i+1]:
        result = A[i]
    break
return result
```

如果使用 Dictionary，自然也可以。
等於是把一個 list 的元素轉換成 key，順便再把次數塞進去當作 value。    
```
dic = {}
for i in A:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

count = len(A) // 2
for key, value in dic.items():
    if value == count:
        return key
```
建玩 Dictionary 後，構建判斷邏輯，    
題目說了，List 長度為偶數個，且重複的元素有 2N，這個是前提。
因此邏輯如下：
```
count = len(A) // 2
for key, value in dic.items():
    if value == count:
```

