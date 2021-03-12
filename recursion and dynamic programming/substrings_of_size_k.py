'''Find all unique substrings containing distinct characters of length k given a string s containing
only lowercase alphabet characters.
Input: s = xabxcd, k = 4
Output: ["abxc", "bxcd"]
Explanation:
The substrings are xabx, abxc, and bxcd. However x repeats in the xabx, so it is not a valid substring of a distinct characters.
'''

# create a hash table
# iterate through string s storing chars in hash table and keeping track of start and end
# if char is in hash table, iterate start until it gets to equal char and move one more
# pop all chars as you go
# then move end until end index - start index == k and continue

def find_subs(s, k):
    if len(s)< k:
        return
    book = {}
    start= end = 0
    result = set()
    while end < len(s):
        value = s[end]
        if value in book:
            print(value,book, start, end, book[value]+1)
            while start < book[value]:
                book.pop(s[start])
                start+=1
            book[value]= end
            start+=1
        else:
            book[value] = end
        if end-start ==k-1:
            sub = s[start:end+1]
            if sub not in result:
                result.add(sub)
            book.pop(s[start])
            start+=1
        end += 1
    return result

s = "aabcdbcd"; k = 3
find_subs(s,k)