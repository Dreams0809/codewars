def get_count(sentence):
    
    count = 0
    
    for vowel in sentence:
        if vowel in 'aeiou':
            count += 1
    return count
        