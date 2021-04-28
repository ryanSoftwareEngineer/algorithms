'''
We are given some website visits: the user with name username[i] visited the website website[i] at time timestamp[i].

A 3-sequence is a list of websites of length 3 sorted in ascending order by the time of their visits.  (The websites in a 3-sequence are not necessarily distinct.)

Find the 3-sequence visited by the largest number of users. If there is more than one solution, return the lexicographically smallest such 3-sequence.

Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
Output: ["home","about","career"]
Explanation:
The tuples in this example are:
["joe", 1, "home"]
["joe", 2, "about"]
["joe", 3, "career"]
["james", 4, "home"]
["james", 5, "cart"]
["james", 6, "maps"]
["james", 7, "home"]
["mary", 8, "home"]
["mary", 9, "about"]
["mary", 10, "career"]
The 3-sequence ("home", "about", "career") was visited at least once by 2 users.
The 3-sequence ("home", "cart", "maps") was visited at least once by 1 user.
The 3-sequence ("home", "cart", "home") was visited at least once by 1 user.
The 3-sequence ("home", "maps", "home") was visited at least once by 1 user.
The 3-sequence ("cart", "maps", "home") was visited at least once by 1 user.
'''
from collections import defaultdict

# store three arrays in one matrix then sort
# for each username find all tuples permutations of their book[username] = [ list of visits ]
# find all by permutations via brute forcing each subset of visits appending count of trio's
# iterate through answers.keys to find greatest count and lowest string
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        triple = sorted(zip(username, timestamp, website))
        book = defaultdict(list)
        for tup in triple:
            book[tup[0]].append(tup[2])

        def get_trios(arr, answers, user):
            visited = set()
            for first in range(len(arr) - 2):
                for second in range(first + 1, len(arr) - 1):
                    for third in range(second + 1, len(arr)):
                        # could we speed this up by skipping duplicates?
                        triplet = (arr[first], arr[second], arr[third])
                        if triplet not in visited:
                            answers[triplet] += 1
                            visited.add(triplet)

            return answers

        answers = defaultdict(lambda: 0)
        for user in book.keys():
            answers = get_trios(book[user], answers, user)

        maxsofar = 0
        answer = None
        for key in answers.keys():
            val = answers[key]
            if val == maxsofar:
                if key < answer:
                    answer = key
            if val > maxsofar:
                maxsofar = val
                answer = key
        return answer