標籤：動態規劃
--
思路
--
後面與前面的最大差值。
```
for i in range(1, len(prices)):
    res = max(res, prices[i] - cur_min)
    cur_min = min(cur_min, prices[i])
```
![image](https://github.com/AvisChiu/Leetcode_Practice/blob/master/121.買股票的最佳時機/stock.gif)

MIN
--
指的是紀錄下掃過的更小的值。
<br/>
收益 res
--
指的是遇到收益更大的，即把當前的收益值覆蓋掉。
