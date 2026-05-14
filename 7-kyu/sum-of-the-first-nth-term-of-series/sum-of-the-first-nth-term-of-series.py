def series_sum(n):
    total = 0
    denominator = 1
    
    for i in range(n):
        total += 1 / denominator
        denominator += 3
    
    return f"{total:.2f}"