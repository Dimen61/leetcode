class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.user_tweet_map = {}
        self.follower_followee_map = {}
        self.tweet_time_map = {}
        self.tweet_time_count = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId in self.user_tweet_map:
            self.user_tweet_map.get(userId).append(tweetId)
        else:
            self.user_tweet_map[userId] = [tweetId]

        self.tweet_time_count += 1
        self.tweet_time_map[tweetId] = self.tweet_time_count

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        MOST_RECENT = 10
        news = self.user_tweet_map.get(userId, [])[:]
        
        for user in self.follower_followee_map.get(userId, []):
            news.extend(self.user_tweet_map.get(user, []))
        
        news = list(set(news))
        news.sort(key=lambda x: self.tweet_time_map[x], reverse=True)

        return news[:MOST_RECENT]

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.follower_followee_map:
            self.follower_followee_map[followerId].append(followeeId)
        else:
            self.follower_followee_map[followerId] = [followeeId]
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if not followerId in self.follower_followee_map:
            return
        else:
            if followeeId in self.follower_followee_map[followerId]:
                self.follower_followee_map[followerId].remove(followeeId)

# An much conciser solution!
import itertools, collections, heapq

class Twitter(object):

    def __init__(self):
        self.count_it = itertools.count(step=-1)
        self.tweets = collections.defaultdict(collections.deque)
        self.followees = collections.defaultdict(set)

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.tweets[userId].appendleft((next(self.count_it), tweetId))

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        tweets = heapq.merge(*(self.tweets[user]
                               for user in self.followees[userId] | {userId}))
        return [t for _, t in itertools.islice(tweets, 10)]


    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.followees[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)



# twitter = Twitter();

# # // User 1 posts a new tweet (id = 5).
# twitter.postTweet(1, 5);
# print(twitter.user_tweet_map)

# # // User 1's news feed should return a list with 1 tweet id -> [5].
# twitter.getNewsFeed(1)
# print(twitter.user_tweet_map)

# # // User 1 follows user 2.
# twitter.follow(1, 2);
# print(twitter.user_tweet_map)

# # // User 2 posts a new tweet (id = 6).
# twitter.postTweet(2, 6);
# print(twitter.user_tweet_map)

# # // User 1's news feed should return a list with 2 tweet ids -> [6, 5].
# # // Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# twitter.getNewsFeed(1)
# print(twitter.user_tweet_map)

# # // User 1 unfollows user 2.
# twitter.unfollow(1, 2);
# print(twitter.user_tweet_map)

# # // User 1's news feed should return a list with 1 tweet id -> [5],
# # // since user 1 is no longer following user 2.
# print(twitter.getNewsFeed(1))
# # print(twitter.user_tweet_map)


twitter = Twitter()
twitter.postTweet(1, 5)
twitter.postTweet(1, 3)
print(twitter.getNewsFeed(1))
# print(twitter.tweet_time_map)