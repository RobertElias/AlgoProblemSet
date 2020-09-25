def merge_packages(items, limit):
    pair = []
    if(items == None):
        return 0
    for i in range(len(items)):
        remain = limit - items[i]
        if(remain in items[i:]):
            ind = items.index(remain)
            pair.append(ind)
            pair.append(i)
            break
    
    return pair