思路：
--
題目要求：二分法   
先思考從哪裡到哪裡二分。     
```
x < (x/2)^2 + 1
```
一個數的平方根一定比這個書的一半加一小。     
因此二分的距離就是從 1 ～ (x/2)^2 + 1     
所以但 數字 的平方大於 x 的時候，答案就是 (數字-1)

```
left = 1 
right = x//2 
while left < right:
    mid = (left + right + 1) // 2 
    square = mid*mid
    if square > x:
        right = mid - 1
    else:
        left = mid
return left
```
Note
---
```
mid = (left + right + 1) // 2 
```
對於這行的理解：這裡是取中位數。想像如下當 x = 9
```
1   2   3   4
```
若按照 (left + right) // 2 這樣取，自己跳到 2，剛好漏掉答案    
意思就是要往考 right 的方向取，再思考如下：
```
1   2   3   4   5   6   7   8   9   10
```
本來中位數是 5 ，但現在要取到 6， 因此方法就是：
```
mid = (left + right + 1) // 2 
```
