思路
--
先把 List 排好序的話，接下來就不會很難。    
於是直接用 sort 去排序，省了很多功夫。    
```
nums.sort()
nums[:] = nums[::-1]
```
</br>

*邏輯*
<br/>
先立一個 flag，接著歷遍整個 List，    
如果當前的數比下一個大的話，flag + 1
停止條件就是 flag == 2
```
for i in range(len(nums)-1):
    if nums[i] >  nums[i+1]:
        flag += 1
        if flag == 2:
            return nums[i+1]
```
會出現下面的情形：不存在第三大的數，要求返回最大的數。
```
[1,1,2]
[2,2,2,2,1]
```
那麼是直接返回 第 0 位
```
return nums[0]
```
