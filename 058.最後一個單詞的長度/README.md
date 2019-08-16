思路：
--
這道題目非常簡單，如果熟悉基本的 List 的操作的話。   
直接用 split 解決。    
</br>

```
tmp = s.split()
if len(tmp) == 0:
    return 0
return(len(tmp[-1]))
```

不用任何工具的話，就要從一種特殊狀況入手:    
即當字串末尾為空格的情況。    
具體解決辦法如下（參考了題解）     



```
end = len(s) - 1
while end >= 0 and s[end] == " ":
    end -= 1
if end == -1: return 0
    start = end
while start >= 0 and s[start] != " ":
    start -= 1
return end - start
```


*解釋*   
從末位開始歷邊，找到第一個不是空格的位置，即 end。       
然後設置一個指標 start = end，    
用來從尾到頭歷邊不是空格的元素。    


```
while start >= 0 and s[start] != " ":
    start -= 1
```


最後的答案就是，start 走了多少步，回看 end 的位置。   
兩者的差即為最後一個單詞的長度。
