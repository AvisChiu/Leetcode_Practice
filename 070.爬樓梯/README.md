標籤：動態規劃
--
思路
--
1. 題目問得是多少種走法，*因此就不要糾結於走一步還是走兩步。*

```
dp = []     // 全部塞進一個 List ，位置代表第幾階，元素代表多少種走法
dp.append(1)
dp.append(2)
    for i in range(2,n):
        dp.append(dp[i-1]+dp[i-2]) // 差一步的走法 + 差兩步的走法
```
<div align=center> <img src="https://github.com/AvisChiu/Leetcode_Practice/blob/master/070.爬樓梯/70爬樓梯.PNG" width="800",height="800"/></div>
