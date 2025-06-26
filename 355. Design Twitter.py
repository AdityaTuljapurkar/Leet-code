from typing import List
from collections import defaultdict
import heapq

class Twitter:
    def __init__(self):
        self.count = 0
        self.follow_map = defaultdict(set)  # follower -> set(followees)
        self.tweet_map = defaultdict(list)  # user -> list of [count, tweetId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minheap = []
        self.follow_map[userId].add(userId)
        for followeeId in self.follow_map[userId]:
            if followeeId in self.tweet_map and self.tweet_map[followeeId]:
                index = len(self.tweet_map[followeeId]) - 1
                count, tweetid = self.tweet_map[followeeId][index]
                heapq.heappush(minheap, (count, tweetid, followeeId, index - 1))
        while minheap and len(res) < 10:
            count, tweetid, followeeId, index = heapq.heappop(minheap)
            res.append(tweetid)
            if index >= 0:
                count, tweetid = self.tweet_map[followeeId][index]
                heapq.heappush(minheap, (count, tweetid, followeeId, index - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId] and followeeId != followerId:
            self.follow_map[followerId].remove(followeeId)

# Example usage:
twitter = Twitter()
twitter.postTweet(1, 5)
twitter.postTweet(1, 3)
print(twitter.getNewsFeed(1))  # Output: [3, 5]
