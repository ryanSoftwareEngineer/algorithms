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

# matrix = []
# row = [0, 0]
# for i in range(2):
#     matrix.append(row)
# print(matrix)
# matrix[1][1] = 1
# print (matrix)
def factory():
    values = []
    def widget(value):
        values.append(value)
        return values
    print(values)
    return widget
'''
widget has it's own state 
'''
worker = factory()
worker(1)
worker(2)
print(worker(4))
print(2%3)
print(1//2)
print([4]+ [3])