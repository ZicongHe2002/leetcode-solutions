class Solution:
    def findRestaurant(self, list1, list2):
        positions = {name: index for index, name in enumerate(list1)}
        best = len(list1) + len(list2)
        result = []
        for second_index, name in enumerate(list2):
            first_index = positions.get(name)
            if first_index is None:
                continue
            total = first_index + second_index
            if total < best:
                best = total
                result = [name]
            elif total == best:
                result.append(name)
        return result
