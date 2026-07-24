class Twitter:

    def __init__(self):
        self.timestamp = 0

        # stores each user's tweets
        self.tweets = defaultdict(list)

        # stores WHO each user follows
        self.follower = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # storing each user's own tweets
        self.tweets[userId].append([self.timestamp, tweetId])
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # get news feed from userId AND news feed of who userId follows
        res = []
        min_heap = []
        
        # go through everyone including yourself
        self.follower[userId].add(userId)
        for followee in self.follower[userId]:
            if followee in self.tweets:
                index = len(self.tweets[followee]) - 1
                timestamp, tweetId = self.tweets[followee][index]
                heapq.heappush(min_heap, [timestamp, tweetId, followee, index - 1])
        
        # merge tweet lists
        while min_heap and len(res) < 10:
            timestamp, tweetId, followee, index = heapq.heappop(min_heap)
            res.append(tweetId)
            if index >= 0:
                time, tweetId = self.tweets[followee][index]
                heapq.heappush(min_heap, [time, tweetId, followee, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower[followerId]:
            self.follower[followerId].remove(followeeId)
        #self.follower[followerId].discard(followeeId)
