思路：
--
使用雙指標，跟 026 一樣：
當 List 長度為 1 的時候，先判斷兩種特殊情況。
```
if len(nums) == 1 and nums[0] != val:
    return 1
if len(nums) == 1 and nums[0] == val:
    return 0
```

構造邏輯:
```
pin = 0
for i in range(len(nums)):
    if nums[i] != val:
        nums[pin] = nums[i]
        pin = pin + 1              
return pin 
```
意思就是說，正常歷邊 List，如果元素不等於禁忌值，則 指標跟著一起滑動。   
若元素等於禁忌值，則把指標留在當前位置。

![image](https://github.com/AvisChiu/Leetcode_Practice/blob/master/027.%E7%A7%BB%E9%99%A4%E5%85%83%E7%B4%A0/027.gif)
