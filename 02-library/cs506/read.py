def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    page = open(csv_file_path)
    lines = page.readlines()
    X = []
    for line in lines:
        xlist = line.split(',')
        xlist = [int(x) if (x.strip()).isnumeric() else x.strip("\"") for x in xlist]
        X.append(xlist)
    return X
