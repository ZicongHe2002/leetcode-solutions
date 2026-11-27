class Solution:
    def invalidTransactions(self, transactions):
        parsed = []
        for record in transactions:
            name, time, amount, city = record.split(',')
            parsed.append((name, int(time), int(amount), city))
        invalid = []
        for index, (name, time, amount, city) in enumerate(parsed):
            conflict = amount > 1000
            for other_name, other_time, _, other_city in parsed:
                if name == other_name and city != other_city and abs(time - other_time) <= 60:
                    conflict = True
                    break
            if conflict:
                invalid.append(transactions[index])
        return invalid
