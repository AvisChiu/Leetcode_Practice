思路：
--
不考慮時間複雜度和空間複雜度的話非常簡單。  
以下是忽略時間複雜度的想法：   
```
pin = "xxxx"
for i in range(len(nums)-1):
    if nums[i] == nums[i+1]:
        nums[i] = pin              
while pin in nums:
    nums.remove(pin) 
```
在 List 裡面逐位對比，若當前的元素與下一位相同，則把當前的元素修改為字符 “xxxx”。   
最後生成一個數字不重複，且存在很多 “xxxx” 的 List。   
再移除所有 “xxxx” 的項即可。
最後回傳 List 的長度。  

*這個辦法時間複雜度不符合題目原意*
--
還有一個辦法就是新創建一個 List ,這個辦法不符合空間複雜度為 O(1) 的要求。   

正確解法：
--
題目具有一定誤導，其實正確解法最後看生成的 List ，並沒有刪除任何一個元素。   
也就是說長度沒有改變，只是在現有的 List 中，構造一個正確的排序。
```
if (len(nums) == 0):
    return 0
i = 0
for j in range(len(nums)):
    if (nums[j] != nums[i]):
      i = i + 1
      nums[i] = nums[j]
```

