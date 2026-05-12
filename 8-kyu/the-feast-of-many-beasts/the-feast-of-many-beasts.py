def feast(beast, dish):
    # your code here
    #the dish must start and end witht he same letter as the animal's name 
    if beast[0] == dish[0] and beast[-1] == dish[-1]:
        return True
    else: 
        return False
    
    pass