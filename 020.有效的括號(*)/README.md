思路：
--
開始用 rule based，放棄。    
遂參考評論的解法，看到一個挺巧妙的解法，但運行效率比較慢。   
(每次都刪掉一個，填入空白。)
```
a = '()'
b = '{}'
c = '[]'
while a in s or b in s or c in s:
    s = s.replace(a,'')
    s = s.replace(b,'')
    s = s.replace(b,'')
```
*方法二：*
構造字典 Dictionary
```
dic = {}
dic["("] = 1
dic[")"] = -1
dic["["] = 2
dic["]"] = -2
dic["{"] = 3
dic["}"] = -3
```
生成一個 List ，之後作業都在 List 上面做。   

<div align=center> <img src="https://https://github.com/AvisChiu/Leetcode_Practice/blob/master/020.%E6%9C%89%E6%95%88%E7%9A%84%E6%8B%AC%E8%99%9F(*)/figure1.png" width="800",height="800"/></div>  

