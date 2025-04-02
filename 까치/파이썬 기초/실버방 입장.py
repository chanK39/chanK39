dataset = [ 
    {"tier": "Bronze", "lane": "Top", "champion": "Gangplank"}, 
    {"tier": "Bronze", "lane": "Middle", "champion": "Ahri"}, 
    {"tier": "Silver", "lane": "Middle", "champion": "Yasuo"}, 
    {"tier": "Silver", "lane": "Jungle", "champion": "Graves"}, 
    {"tier": "Gold", "lane": "Jungle", "champion": "Warwick"},
    {"tier": "Gold", "lane": "Bottom", "champion": "Lux"} 
]  
    
for data in dataset:
    if data["tier"] == "Bronze":
        if data["lane"] == "Middle": 
            print(len(data["champion"])) 
            
    else: 
        if data["lane"] != "Jungle": 
            print(len(data["champion"]))