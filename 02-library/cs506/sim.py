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
    intersect = len(set(x).intersection(set(y)))
    print('intersect: {i}'.format(i=intersect))
    union = (len(x) + len(y)) - intersect
    similarity = intersect/union
    return 1 - similarity
    

def cosine_sim(x, y):
    raise NotImplementedError()

# Feel free to add more
