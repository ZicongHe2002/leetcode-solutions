class Solution:
    def numMusicPlaylists(self, n, goal, k):
        modulus = 10**9 + 7
        ways = [0] * (n + 1)
        ways[0] = 1
        for length in range(1,goal + 1):
            following = [0] * (n + 1)
            for used in range(1,min(n,length) + 1):
                new_song = ways[used - 1] * (n - used + 1)
                replay = ways[used] * max(0,used - k)
                following[used] = (new_song + replay) % modulus
            ways = following
        return ways[n]
