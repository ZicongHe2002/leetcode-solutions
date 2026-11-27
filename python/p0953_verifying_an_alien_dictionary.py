class Solution:
    def isAlienSorted(self, words, order):
        rank = {char:index for index,char in enumerate(order)}
        for index in range(1,len(words)):
            first,second = words[index - 1],words[index]
            for left,right in zip(first,second):
                if left != right:
                    if rank[left] > rank[right]:
                        return False
                    break
            else:
                if len(first) > len(second):
                    return False
        return True
