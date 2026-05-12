geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    result = []
    for birds in birds:
        if birds not in geese:
            result.append(birds)
    return result
        