class Solution:
    def flipLights(self, n, presses):
        width = min(n, 6)
        masks = [0, 0, 0, 0]
        for label in range(1, width + 1):
            bit = 1 << (label - 1)
            masks[0] |= bit
            masks[1 if label % 2 == 0 else 2] |= bit
            if label % 3 == 1:
                masks[3] |= bit
        states = set()
        for parity in range(16):
            count = parity.bit_count()
            if count > presses or (presses - count) % 2:
                continue
            state = (1 << width) - 1
            for button in range(4):
                if parity & (1 << button):
                    state ^= masks[button]
            states.add(state)
        return len(states)
