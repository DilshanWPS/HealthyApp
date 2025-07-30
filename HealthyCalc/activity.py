def ActMultiplier(activity_level):
    levels = {
        "1": 1.2,   
        "2": 1.375, 
        "3": 1.55,  
        "4": 1.725, 
        "5": 1.9    
    }
    return levels.get(activity_level, 1.2)
