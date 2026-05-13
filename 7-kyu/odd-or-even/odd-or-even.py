def odd_or_even(arr):
    if not arr:
        arr = [0]
    
    if sum(arr) % 2 != 0:
        return "odd"
    else: 
        return "even"
​
  