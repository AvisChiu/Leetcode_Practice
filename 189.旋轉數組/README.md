思路
--
沒有要求的話應該是非常簡單的一道題，    
pop + insert 直接就做完了。
```
for i in range(k):
    tmp = nums.pop()
    nums.insert(0,tmp)
```
題目說其實有很多種辦法可以做，    
於是參考了一些別人的作法。    
```
n = len(nums)
k %= n
nums[:] = nums[::-1]
nums[:k] = nums[:k][::-1]
nums[k:] = nums[k:][::-1]
```
反轉的作法有點想不到，看了之後才意識到原來可以這樣做。     
先降序，再分段升序。
