def persistence(num):
    count = 0
    while num >= 10:        # keep going until single digit
        digits = [int(d) for d in str(num)]  # split into digits
        product = 1
        for d in digits:
            product *= d    # multiply them all together
        num = product       # the result becomes the new number
        count += 1          # that was one round
    return count
        