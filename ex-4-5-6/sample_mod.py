def recaman(max_terms):
    exist = set()
    seq=list()
    n = 0 
    a = 0
    while n < max_terms:
        diff=a-n
        if diff > 0 and diff not in exist:
            a = diff
        else:
            a = a + n
        exist.add(a)
        seq.append(a)
        n += 1
    return seq

def recaman2(max_terms):
    seq=list()
    n = 0 
    a = 0
    while n < max_terms:
        diff=a-n
        if diff > 0 and diff not in seq:
            a = diff
        else:
            a = a + n
        seq.append(a)
        n += 1
    return seq