
import random

def get_numbers_ticket(min, max, quantity): 
    if type(min) is not int or type(max) is not int or type(quantity) is not int:
        return ValueError("enter valid values")
    if min > max: 
        return ValueError("max should be greater than min") 
    if quantity < 1:
        return ValueError("quantity should be greater 0") 
    result = []
    while len(result) < quantity:
        generated = random.randint(min, max)
        if generated not in result:
            result.append(generated)
    result.sort()
    return result

print(get_numbers_ticket(1, 49, 6))
print(get_numbers_ticket("a", 49, 6))
print(get_numbers_ticket(99, 49, -6))
print(get_numbers_ticket(-99, 49, -6))