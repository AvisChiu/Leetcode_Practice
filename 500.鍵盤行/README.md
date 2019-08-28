思路
--
題目要求用哈希表，
算是一道蠻講究邏輯的題目。

**第一步**
先構造一個 Dictionary ,
key 代表鍵盤的上中下三行，value 是一個 List，裝了每一行的元素。
```
dic["up"] = ["Q","W","E","R","T","Y","U","I","O","P","q","w","e","r","t","y","u","i","o","p"]
dic["mid"] = ["A","S","D","F","G","H","J","K","L","a","s","d","f","g","h","j","k","l"]
dic["down"] = ["Z","X","C","V","B","N","M","z","x","c","v","b","n","m"]
```

**第二步**
邏輯：    
就只拿字串的第一個字母來判斷屬於鍵盤上面的第幾行。    
例如 “ Hello “ ，那麼 flag = ”mid“
```
for items in words:
    flag =""
    if items[0] in dic["up"]:
        flag = "up"
    elif items[0] in dic["mid"]:
        flag = "mid"
    elif items[0] in dic["down"]:
        flag = "down"
```
**第三步**
沒多想，設定了一個指針，其實應該有別的方法。    
對一個字串進行歷邊，如果所有字母在 *dictionary[flag]* 說明這個字串是我們需要的。   
判斷邏輯就是 每次對比符合要求，pin 加 1，最後判斷 pin 是否等於 整個字母的長度。    
是的話 append 到一個新的 List。
```
pin = 0
for term in items:
    if term in dic[flag]:
        pin = pin + 1
    if pin == len(items):
        new.append(items)
```

*Note*
--
這道題目沒有什麼需要轉彎的地方，直覺上也沒有什麼巧妙的技巧。    
因此一步一步坐下去就能出結果了。

