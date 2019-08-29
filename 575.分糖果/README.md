思路
--
先構建一個 Dictionary，key 為糖果種類， value 為某一種糖果的數量。   
注意 Dictionary 奇妙的建構方法。
```
dic = {}
for i in candies:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
```
構造判斷邏輯：    
先把每個人分到的糖果數量算出， 即 average，    
再把一共有多少總糖果算出，即 cata 。     
</br>
例如，糖果種類為 3 ， 總糖果數為 8 ，理所當然，最多獲得 3 種。   
若 糖果種類為 3 ，糖果總數為 4 ，理所當然獲得 2 種。    
總結，先看能分多少糖果，再看一共多少種類。
```
average = len(candies) / 2 
cata = len(dic.keys())
if average < cata:
    return average
else:
    return cata
```

