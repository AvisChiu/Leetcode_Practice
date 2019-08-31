思路
--
很簡單的一道題，一樣是做一個 Dictionary。
Key 為單詞， Value 為次數。    
最後把那些 次數為 1 的挑出來。     

Note
--
做 Dictionary 之前要對字串進行處理。
```
A = A.split()
B = B.split()
```
```
for key, value in dicA.items():
    if value == 1:
        result.append(key)
```
