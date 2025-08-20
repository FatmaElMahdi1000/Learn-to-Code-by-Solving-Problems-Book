def order(burger, SideOrder, Drink, Dessert):
    """
    method to calculate the total number of calories intake
    Params: 
        takes users' inputs from burger, SideOrder, Drink, Dessert
    Returns:
        int: total number of calories 
    """
    Total_calories = 0
    burger_hash_map = {"1" : 461, "2": 431, "3":420, "4": 0}
    SideOrder_hash_map = {"1" : 100, "2": 57, "3":70, "4": 0}
    Drink_hash_map = {"1" : 130, "2": 160, "3":118, "4": 0}
    Dessert_hash_map = {"1" : 167, "2": 266, "3":75, "4": 0}
    if burger in burger_hash_map:
        Total_calories = Total_calories + burger_hash_map[burger]
    else:
        return "invalid input"
    if SideOrder in SideOrder_hash_map:
        Total_calories = Total_calories + SideOrder_hash_map[SideOrder]
    else:
        return "invalid input"
        
        
    if Drink in Drink_hash_map:
        Total_calories = Total_calories + Drink_hash_map[Drink]
    else:
        return "invalid input"
        
    if Dessert in Dessert_hash_map:
        Total_calories = Total_calories + Dessert_hash_map[Dessert]
    else:
        return "invalid input"
    return f"Your total Calorie count is {Total_calories}."
        
burger = input()
SideOrder = input()
Drink = input()
Dessert = input()
print(order(burger, SideOrder, Drink, Dessert))
