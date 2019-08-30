思路
--
對這道題目無言以對，
邏輯簡單，但是感覺很難想清楚。     

判斷兩類
--
一、完全用完給的車牌號裡面的字母。   
二、沒有完全用車牌號裡面的字母。
</br>


*第一類：完全用完給的車牌號裡面的字母*
--
先做一個 Dictionary ，key 是車牌的字母，value 是出現次數。
```
dic = {}
licensePlate = str(licensePlate.lower())  // 換小寫
licensePlate = filter(str.isalpha, licensePlate)  // 去掉數字
        
for i in licensePlate :
    if i in dic and i != ' ':     // 去掉空格
        dic[i] += 1
    if i not in dic and i != ' ':
        dic[i] = 1
```
*判斷邏輯：  （字典裡面有多少個 value = 0）*    
```
for j in words:
    dicc = dic.copy()           //  copy 一份 Dictionary
    for i in range(len(j)):     //  對每一個單詞的字母歷邊
        if j[i] in dic and dicc[j[i]] != 0:   
            dicc[j[i]] -= 1     // 若在 dictionary 裡面，字典的 value 減 1， 只能減到 0 ！！！！
            
    result = dicc.values().count(0)     // 計算 字典裡面有多少個 value = 0
    if result == countzero:     // countzero 等於車牌字母的數量。 （全部為 0 說明剛好配對）
        if len(new) == 0:
            new.append(j)
        elif len(j) < len(new[0]):    // 如果有符合但是長度更短的，把這個替換掉原來的
            new.pop()                 // List 裡面只能留一個 ～！！！！！！！
            new.append(j)             
```

*第二類：沒有完全用車牌號裡面的字母*
--
*判斷邏輯：  計算字典裡面 value 的和 （和越小說明用的字母越多）*    
```
if len(new) == 0:             // 如果 new 沒東西，說明沒有完美符合的，這就開始考慮第二類。
for j in words:               
    dicc = dic.copy()
    for i in range(len(j)):   
        if j[i] in dic and dicc[j[i]] != 0:     // 一樣是減 1
            dicc[j[i]] -= 1
    result = sum(dicc.values())                 // 這次是開始計算字典裡面 value 的和 （和越小說明用的字母越多）
```
  
```
if len(neww) == 0:
    neww.append(j)
    neww.append(result)
                    
if len(neww) != 0:
    if result < neww[1]:    // List 裡面只存兩個，第一個是 單詞，第二個是 “和”
    neww.pop()              // 碰到 “和” 更小的，把原先的替換
    neww.pop()
    neww.append(j)
    neww.append(result)
```
