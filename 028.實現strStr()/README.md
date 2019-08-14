思路：
--
做過026、027之後會覺得這道題非常簡單，    
同樣是用到雙指標。
```
pin = 0
for i in range(len(haystack)-len(needle)):
    if haystack[i:i+len(needle)] == needle:   # 如果找到相同的，則跳出。
        break
    if haystack[i:i+len(needle)] != needle:   # 若不相同，指標加一。
        pin = pin + 1
```
*Note*
1. 歷邊 haystack 的時候，需要注意到底要歷邊多少次：len(haystack)-len(needle)   
2. 主要思想就是，當前若不相同，i 往下走一位，指標 pin 也跟著往下走一位。
```
if haystack[i:i+len(needle)] != needle:   # 若不相同，指標加一。
    pin = pin + 1
```
