#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
from collections import defaultdict,deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def bfs(word):
            q=deque([word])
            visited=defaultdict(bool)
            count=defaultdict(lambda:10**8)
            count[word]=1
            n=len(word)
            del_dict=defaultdict(list)
            for w in wordList:
                for i in range(n):
                    del_dict[w[:i]+"*"+w[i+1:]].append(w)
            while q:
                word=q.popleft()
                if word==endWord:continue
                for i in range(n):
                    temp=word[:i]+"*"+word[i+1:]
                    for w in del_dict[temp]:
                        if not visited[w] and count[w]>count[word]+1:
                            visited[w]=True
                            count[w]=count[word]+1
                            q.append(w)
            res=0 if count[endWord]==10**8 else count[endWord]
            return res
        return bfs(beginWord)            

# @lc code=end
