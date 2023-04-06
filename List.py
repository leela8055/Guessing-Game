# Module to create a list of numbers
def List(p, q):

    if p == q:
        return p
    else:
        list = []

        while p < q + 1:
            list.append(p)
            p = p + 1
        return list
