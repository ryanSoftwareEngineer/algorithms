


# fast attempt one. Lots of extra memory and extra iterations but done in <45 min having never seen it before so who fucking cares
def getMinScore(product_nodes, product_edges, products_from, products_to):
    # store products to in set if
    trios = {}
    book = {}
    for i, b in enumerate(products_from):
        a = products_to[i]
        if b in book:
            book[b].append(a)
        else:
            book[b] = [a]
        if a in book:
            book[a].append(b)
        else:
            book[a] = [b]
    nonleaves = set()
    for i in book:
        if len(book[i]) >1:
            nonleaves.add(i)
    for c in book:
        if c in nonleaves:
            path, ans = get_trio(c, book, set())
            if ans is True:
                if tuple(path) not in trios:
                    trios[tuple(path)] = path
    mini = 2**32
    for key in trios:
        score = 0
        for j in key:
            for val in book[j]:
                print(j, val, key, nonleaves, score)
                if val not in nonleaves:
                    score+= 1
        mini = min(score, mini)
    return mini



def get_trio(node, book, visited):
    if node not in book or len(book[node])<2:
        return visited, None
    if len(visited) > 3:
        return visited, False
    if node in visited:
        return visited, True
    visited.add(node)
    ans = None
    for i in book[node]:
        if len(book[i]) >1:
            visited, ans = get_trio(i, book, visited)
        if ans is False:
            visited.remove(i)
    if ans is None:
        ans = False
    return visited, ans

products_nodes = 6
products_edges = 6
products_from = [1,2,2,3,4,5]
products_to = [2,4,5,5,5,6]
getMinScore(products_nodes, products_edges, products_from, products_to)