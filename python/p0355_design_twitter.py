from heapq import heapify, heappop, heappush


class Twitter:
    def __init__(self):
        self._clock = 0
        self._posts = {}
        self._following = {}

    def postTweet(self, userId, tweetId):
        self._posts.setdefault(userId, []).append((self._clock, tweetId))
        self._clock += 1

    def getNewsFeed(self, userId):
        authors = self._following.get(userId, set()) | {userId}
        heap = []
        for author in authors:
            posts = self._posts.get(author)
            if posts:
                index = len(posts) - 1
                heap.append((-posts[index][0], author, index))
        heapify(heap)
        feed = []
        while heap and len(feed) < 10:
            _, author, index = heappop(heap)
            posts = self._posts[author]
            feed.append(posts[index][1])
            if index:
                index -= 1
                heappush(heap, (-posts[index][0], author, index))
        return feed

    def follow(self, followerId, followeeId):
        self._following.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId, followeeId):
        self._following.get(followerId, set()).discard(followeeId)
