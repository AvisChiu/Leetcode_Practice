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
<br/>

MIN
--

指的是紀錄下掃過的更小的值。  
<br/>

收益 res
--
指的是遇到收益更大的，即把當前的收益值覆蓋掉。

<br/>
<br/>
<br/>


```
income = 0
pin = prices[0]
        
for i in range(1,len(prices)):
    if prices[i] - pin > income:        // 如果當前的元素 減去 當前的最小值得 有更大收益
        income = prices[i] - pin        // 把最大收益覆蓋
    if prices[i] < pin:                 // 如果當前的元素 比 當前的最小值更小
        pin = prices[i]                 // 把當前的最小值覆蓋 （指針往後移動）
                
```

<br/>

```
[7,3,6,2,5]
```
一直找尋找最小的數字，因此會找到 2 ,但最大收益並不變。    
一直找最小就是為了防止後面還有很大的數字。

