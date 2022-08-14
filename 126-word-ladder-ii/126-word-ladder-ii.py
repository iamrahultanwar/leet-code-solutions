from collections import defaultdict, deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        adj = defaultdict(list)
        # Create Adjacency List
        for word in wordList:
            for i in range(len(word)):
                h = word[:i]+'#'+word[i+1:]
                adj[h].append(word)
        
        # The set of parents that create a word in the fastest way
        parents = defaultdict(set)  
        # BFS queue with word and distance
        q = deque([(beginWord,0)])
        # seen/visited hashmap storing the minimum distance to get key word from beginWord
        seen = {beginWord:0}
        # minimum distance to get endWord
        minDist = float('inf')
        
        # RUN BFS, to create the parents dictionary
        while q:
            word,dist = q.popleft()
            # For each character change
            for i in range(len(word)):
                h = word[:i]+'#'+word[i+1:]
                # For each word adjacent to the hash
                for neighbor in adj[h]:
                    # make sure the word has not been visited
                    # & neighbor distance is less than or equal to minimum distance
                    # to get to the endWord
                    if neighbor not in seen or seen[neighbor]==dist+1<=minDist:
                        # set minDist is endWord encountered
                        if neighbor==endWord:minDist = dist+1
                        # add word as the neighbor, since we want all min parents
                        parents[neighbor].add(word)
                        # visit the neighbor
                        if neighbor not in seen:
                            seen[neighbor]=dist+1
                            q.append((neighbor,dist+1))
        
        # free unwanted variables
        del adj,seen
        
        answers = []
        def makeSequences(word,seq):
            """ Makes sequences from the parent dictionary """
            if word==beginWord:
                # reverse sequence since we started from the end
                answers.append(seq[::-1])
            else:
                # iterate for all parents
                for parent in parents[word]:
                    makeSequences(parent,seq+[parent])
        # call make sequences
        makeSequences(endWord,[endWord])
        return answers