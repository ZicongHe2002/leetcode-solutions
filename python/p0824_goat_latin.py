class Solution:
    def toGoatLatin(self, sentence):
        vowels = set('aeiouAEIOU')
        result = []
        for index,word in enumerate(sentence.split(),1):
            if word[0] not in vowels:
                word = word[1:] + word[0]
            result.append(word + 'ma' + 'a' * index)
        return ' '.join(result)
