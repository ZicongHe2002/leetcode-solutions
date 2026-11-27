class Solution:
    def spellchecker(self, wordlist, queries):
        def vowel_key(word):
            return ''.join('*' if char in 'aeiou' else char for char in word.lower())

        exact = set(wordlist)
        lowercase = {}
        vowels = {}
        for word in wordlist:
            lowercase.setdefault(word.lower(),word)
            vowels.setdefault(vowel_key(word),word)
        answer = []
        for query in queries:
            if query in exact:
                answer.append(query)
            elif query.lower() in lowercase:
                answer.append(lowercase[query.lower()])
            else:
                answer.append(vowels.get(vowel_key(query),''))
        return answer
