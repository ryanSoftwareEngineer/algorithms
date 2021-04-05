'''
Your team is trying to understand customer shopping patterns and offer items that are regularly bought together to new customers. Each item that has been bought together can be represented as an undirected graph where edges join often bundled products. A group of n products is uniquely numbered from 1 of product_nodes. A trio is defined as a group of three related products that all connected by an edge. Trios are scored by counting the number of related products outside of the trio, this is referred as a product sum.

Given product relation data, determine the minimum product sum for all trios of related products in the group. If no such trio exists, return -1.

Example
products_nodes = 6
products_edges = 6
products_from = [1,2,2,3,4,5]
products_to = [2,4,5,5,5,6]

Product	Related Products
1	2
2	1, 4, 5
3	5
4	2, 5
5	2, 3, 4, 6
6	5
A graph of n = 6 products where the only trio of related products is (2, 4, 5).

The product scores based on the graph above are:

Product	Outside Products	Which Products Are Outside
2	1	1
4	0
5	2	3, 6
In the diagram above, the total product score is 1 + 0 + 2 = 3 for the trio (2, 4, 5).
'''


# fast first attempt. I remove any leaf nodes from the graph and did a dfs
# that only travels 3 nodes deep looking for 3 node circles to find triple sets
# i probably did not need to remove leaf nodes first but i thought it would reduce the dfs calls by eliminating
# nodes that can't possibly be in the trio
#
# it was implied that the product id's ranged from 0 to product_nodes-1 but it didn't specify this so I accomplished
# the task without utilizing product_nodes and product_edges data. With this data we could cut
# hash tables in exchange for array's where index = id
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
    mini = 2**31
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