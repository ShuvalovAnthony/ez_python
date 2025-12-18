def f(start, stop):
    if (start > stop) or (156 > start > 150):
        return 0 
    elif start==stop:
        return 1 
    
    return (
        f(start*2, stop)+
        f(start*4, stop)+
        f(start+1, stop)
    )

print(f(36,156))