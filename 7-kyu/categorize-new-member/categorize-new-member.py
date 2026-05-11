def open_or_senior(data): # the thought process of this is that we need an if statement because of the age and handicaps.
   result = [] #showing an empty set of results, becasue that is what we are adding to
   for age, handicap in data: #we are looping through age and members in the dataset
        if age>= 55 and handicap > 7: # if statement condiitonal, because this is the age and handicaps
            result.append("Senior")
        else: 
            result.append("Open")
   return result #we have to retrn the result since it is an empty array
    