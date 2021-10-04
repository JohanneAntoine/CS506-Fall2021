def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += abs(x[i] - y[i])
    return res

def jaccard_dist(x, y):
    print('x, y: ({x}, {y})'.format(x=x, y=y))
    intersect = 0
    for i in range(len(x)):
        if x[i] == y[i]:
            intersect += 1
    print('inter: {union}'.format(union=intersect))
    union = len(y)
    print('union: {union}'.format(union=union))
    similarity = float(intersect)/union if union != 0 else 0
    print('diff: {doff}'.format(doff=1-similarity))
    return 1 - similarity
    

def cosine_sim(x, y):
    top = sum([x[i]**2 * y[i]**2 for i in range(len(x))])
    denom = ((sum([i**2 for i in x])) ** (1/2)) * ((sum([i**2 for i in y])) ** (1/2))
    return top/denom if denom != 0 else 0

# Feel free to add more
