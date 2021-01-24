'''
this script is just for me to test new things i'm learning
'''


# def perm( arr, l, end, result):
#     if l == end:
#         print(arr)
#         return
#     i = l
#     while i <= end:
#         arr[i], arr[l] = arr[l], arr[i]
#         perm(arr, l+1, end, result)
#         arr[i], arr[l] = arr[l], arr[i]
#         i+=1
#
# cand = [2, 5, 7]
# perm(cand, 0, len(cand)-1, set())

s = "abcc"
count = [0] * 26
for c in s:
    b= ord(c) - ord('a')
    a= count[b]
    print(a, b, c, ord(c))
    count[b]+=1
