dic = {}
        
        dic["up"] = ["Q","W","E","R","T","Y","U","I","O","P","q","w","e","r","t","y","u","i","o","p"]
        
        dic["mid"] = ["A","S","D","F","G","H","J","K","L","a","s","d","f","g","h","j","k","l"]
        
        dic["down"] = ["Z","X","C","V","B","N","M","z","x","c","v","b","n","m"]
        
        new = []
        for items in words:
            flag =""
            if items[0] in dic["up"]:
                flag = "up"
            elif items[0] in dic["mid"]:
                flag = "mid"
            elif items[0] in dic["down"]:
                flag = "down"
            
                
            
            pin = 0
            for term in items:
                if term in dic[flag]:
                    pin = pin + 1
                if pin == len(items):
                    new.append(items)
                
                    
        return new