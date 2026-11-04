import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweet_map = defaultdict(list)
        self.follow_map = defaultdict(set)
        

    def postTweet(self, userId: int, twetId: int) -> None:
        self.tweet_map[userId].append((self.time,twetId))
        self.time +=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        max_heap = []

        users = self.follow_map[userId]|{userId}

        for user in users:
            if self.tweet_map[user]:
                index = len(self.tweet_map[user]) - 1
                timestamp,twetId = self.tweet_map[user][index]

                heapq.heappush(max_heap,(-timestamp,twetId,user,index))

        while max_heap and len(result) <10:
            neg_time,tweet_id,user_id,index = heapq.heappop(max_heap)

            result.append(tweet_id)

            next_index = index - 1

            if next_index >=0:
                timestamp,next_tweet_id = self.tweet_map[user_id][next_index]

                heapq.heappush(max_heap,(-timestamp,next_tweet_id,user_id,next_index))

        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follow_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)
        
