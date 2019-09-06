標籤：動態規劃
--

引用一段分析：   

分析：
由于小偷不能偷相邻房屋，因此容易让人联想到对奇数偶数元素求和的方法。但是仔细想想这道题又不能完全用奇偶数的方法，例如[3,1,1,5,1,7,1]这样的房屋排列，无论小偷偷奇数位置的房屋还是偶数位置的房屋都不能偷得最多的钱。所以小偷不是只能偷相隔一间的房屋，还可以选择相隔两间的（这样求和的元素就是奇偶混杂的），但是如果相隔两间以上就没必要了，因为这中间的房屋只要不相隔都是可以偷的。    

</br>
总结：
根据以上分析，我们发现这道题需要使用动态规划算法，偷到第i个房屋可能是跨过了前面两个房屋（第i-3个），也可能是跨过了前面一个房屋（第i-2个）。dp[i]表示偷完第i个房屋持有的总现金，nums[i]表示第i个房屋内的现金    

</br>
作者：wswsdcc
[链接]：(https://leetcode-cn.com/problems/house-robber/solution/jian-dan-yi-dong-de-dong-tai-gui-hua-python-by-wsw/)
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

</br>

* **總結一些步驟**

根據前面的作者分析，盜賊可以跨一個房間或者跨兩個房間。那麼為什麼不可以跨三個房間呢 ？      
<div align=center> <img src="https://github.com/AvisChiu/Leetcode_Practice/blob/master/198.打家劫舍/figure1.png" width="800",height="800"/></div>
分析兩種特殊情況：
1. 沒有房間
2. 少於兩間房間
```
n = len(nums)
if n == 0:
    return 0
if n <= 2:
    return max(nums)
```
</br>
* **因此考慮大於兩間房間的邏輯**

```
pin = 3
dp = [nums[0]] + [nums[1]] + [nums[0] + nums[2]] + [0] * (n-3)  // 基底 [1 2 4 0]
```
</br>
* **原始的記憶體**

<div align=center> <img src="https://github.com/AvisChiu/Leetcode_Practice/blob/master/198.打家劫舍/init.png" width="800",height="800"/></div>
</br>

* **核心邏輯: 每間房子都只看前面跨一步來的和跨兩步來的，把金額加總**

```
while pin < n:
    dp[pin] = max(dp[pin-2]+nums[pin], dp[pin-3]+nums[pin])
    pin += 1
```


