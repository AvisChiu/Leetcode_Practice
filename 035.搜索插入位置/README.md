思路：
--
這道題目非常簡單，如果熟悉基本的 List 的操作的話。   
提供兩個簡單易想的操作:      
</br>

*其一:*   
先判斷 target 在不在 nums, 若在回傳 index 。   
若不在，把 target 塞入 List，接著 sort ，再回傳 index
```
if target in nums:
    return nums.index(target)
else:
    nums.append(target)
    nums.sort()
    if target in nums:
        return nums.index(target)
```
*其二:*  
歷邊 nums，若發現比 target 大的，直接回傳。   
若沒有這說明 target 比任何元素都大，則回傳 len(nums)
```
for i in range(len(nums)):
    if nums[i] >= target:
        return i
return len(nums)
```

Binary Search：
--
題目要求說用二分搜索，算法簡單且容易理解。
```
left = 0
right = len(nums)-1
        
while left <= right:
    mid = (right+left)//2
    if target < nums[mid]:
        right = mid - 1
    elif target > nums[mid]:
        left = mid + 1 
    else:
      return mid
return left
```

![image](https://github.com/AvisChiu/Leetcode_Practice/blob/master/035.%E6%90%9C%E7%B4%A2%E6%8F%92%E5%85%A5%E4%BD%8D%E7%BD%AE/binary_search.gif)
