class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        res = 0
        visited = set([beginWord])
        queue = deque([beginWord])

        sign = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                key = word[:j] + "*" + word[j + 1 :]
                sign[key].append(word)
        
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res + 1
                for j in range(len(word)):
                    key = word[:j] + "*" + word[j + 1 :]
                    for neighbor in sign[key]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
            res += 1
        return 0
        