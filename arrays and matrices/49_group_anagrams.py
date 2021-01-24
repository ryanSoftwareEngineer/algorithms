'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically
using all the original letters exactly once.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''

def groupAnagrams( strs):
    output = []
    map = {}
    map_i = 0
    for i in strs:
        b = i[:]
        b= "".join(sorted(b))
        if b in map:
            output[map[b]].append(i)
        else:
            map[b] = map_i
            output.append([i])
            map_i += 1
    return output

def attempttwo(strs):
    #  iterate through strs
    #  for every iteration of strs iterate through single string
    #  create array 0 to 26 to hold counts
    #  array of 26 from 0 to 26 represents count for each character
    # convert to string of ints or tuple(array)
    # use hash table to store string of counts
    answer = {}
    for word in strs:
        alphabet = [0]*26
        for char in word:
            alphabet[ord(char.lower())-ord('a')] += 1
        str_result = str(alphabet)
        if str_result in answer:
            answer[str_result].append(word)
        else:
            answer[str_result] = [word]
    return list(answer.values())



strs = ["eat","tea","tan","ate","nat","bat"]
print(attempttwo(strs))