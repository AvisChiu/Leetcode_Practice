思路：
--
最簡單的辦法就是用 sort 。    
而且沒有必要考慮 [1,2,3,0,0,0,0,0,0,0,0] 很多 0 的情況。    
不知道為什麼。    
但題目要求用雙指針，    
第一時間想到用 for，但這個辦法不行，for 的話是假設一個快指針和一個慢指針。     
一開始有點難想，答案是用兩個慢指針。   
```
pin1 = 0 
pin2 = 0
```

方法：雙指針
---
先把 nums1 複製一份，隨即清空 nums1，因為要在 nums1 上面動作。
```
new = nums1[:m] 
nums1[:] = []
```
下一步構造邏輯，兩個慢指針的話嘗試用 while     
對比兩個 List 的元素，小的那個加入到 nums1（這很容易理解）    
其次，用可能出現比較兩個一樣的元素，這種情況並沒有影響。照樣 append    

```
while pin1 < m and pin2 < n: 
    if new[pin1] < nums2[pin2]:
        nums1.append(new[pin1])
        pin1 = pin1 + 1
    else: 
        nums1.append(nums2[pin2])
        pin2 = pin2 + 1
```

while 結束之後，需要想到的是，    
</br>

*某一個指針已經把某一個 List 歷邊，但存在另一個還沒有歷邊的 List*
--
找出還沒有歷邊完全的 List，加入到 nums1
```
if pin1 < m:
    nums1[pin1+pin2:] = new[pin1:]
    
if pin2 < n:
    nums1[pin1+pin2:] = nums2[pin2:]
```

