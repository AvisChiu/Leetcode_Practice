思路
--
釐清邏輯之後其實是很簡單額一道題。   
頂部的 1，2 單獨拿出來 append 到 list 
```
if numRows == 0:
    return new
if numRows == 1:
    new.append([1])
    return new
if numRows == 2:
    new.append([1])
    new.append([1,1])
    return new
```
有兩個邏輯需要搞清楚：   
1. 從第三行開始，首位和末尾都是 1，要先解決這個問題。   
2. 第 x 位元素值 = 上一個 list 的 (x-1) 位 + (x) 位      

</br>

根據這個邏輯開始建立 for loop
```
for i in range(2,numRows):
    tmp = []    // 每次都新開一個 List
    for j in range(i+1):
        if j == 0 or j == i:  //解決第一個問題
            tmp.append(1)
        else:
            tmp.append(new[i-1][j-1]+new[i-1][j])   //解決第二個問題
    new.append(tmp)  // 把這個 List append 
```

