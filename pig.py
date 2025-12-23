import random 

def roll():
    """Simulate rolling a six-sided die."""
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

value = roll()
print (value )