def high_and_low(numbers):
    
    #split into spaces first
    numbers_list = numbers.split()
    
    #convert the string into a integers 
    numbers_int = list(map(int,numbers_list))
    
    highest = max(numbers_int)
    lowest = min(numbers_int)
    
    return f"{highest} {lowest}"