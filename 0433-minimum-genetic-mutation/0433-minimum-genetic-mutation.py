from collections import deque

class Solution:
    def minMutation(self, startGene, endGene, bank):
        bank_set = set(bank)

        if (endGene not in bank_set):
            return -1
        
        queue = deque([(startGene, 0)])
        visited = set([startGene])

        element = ['A','C','G','T']

        while queue:
            current, mutations = queue.popleft()

            if current == endGene:
                return mutations

            for i in range(len(current)):
                for elem in element:
                    if current[i] == elem:
                        continue
                    
                    nextGene = current[:i] + elem + current[i+1:]

                    if nextGene in bank_set and nextGene not in visited:
                        visited.add(nextGene)
                        queue.append((nextGene, mutations+1))
        return -1
            


