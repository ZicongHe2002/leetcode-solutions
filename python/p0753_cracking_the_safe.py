class Solution:
    def crackSafe(self, n, k):
        node_count = k ** (n - 1)
        next_digit = [0] * node_count
        nodes, incoming, reverse_digits = [0], [], []
        while nodes:
            node = nodes[-1]
            if next_digit[node] < k:
                digit = next_digit[node]
                next_digit[node] += 1
                nodes.append((node * k + digit) % node_count)
                incoming.append(str(digit))
            else:
                nodes.pop()
                if incoming:
                    reverse_digits.append(incoming.pop())
        return '0' * (n - 1) + ''.join(reversed(reverse_digits))
