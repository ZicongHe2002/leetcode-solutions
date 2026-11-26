class Solution:
    def numberToWords(self, num):
        if num == 0:
            return 'Zero'
        small = ('', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
                 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen',
                 'Seventeen', 'Eighteen', 'Nineteen')
        tens = ('', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety')

        def under_thousand(value):
            words = []
            if value >= 100:
                words.extend((small[value // 100], 'Hundred'))
                value %= 100
            if value >= 20:
                words.append(tens[value // 10])
                value %= 10
            if value:
                words.append(small[value])
            return words

        words = []
        for scale, label in ((10**9, 'Billion'), (10**6, 'Million'), (1000, 'Thousand'), (1, '')):
            group, num = divmod(num, scale)
            if group:
                words.extend(under_thousand(group))
                if label:
                    words.append(label)
        return ' '.join(words)
