class Twitter:
    """

        store postTweet in some list for receny

        getNewFeed -> gets atmost 10 tweet by time desc (filter by user followed)


        follower_id -> [list of posted tweets]

        Posts map => u1 - [(time, tweetId)]
                     u2 -[(time, tweetId)]

        dict -> user_id = [follower_id]

        getAllFollowers = follow_map[followerId]
        post = []
        for each follower:
            post.append(..)


    """
    def __init__(self):
        
        self.posts = defaultdict(list)
        self.follows = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time, tweetId))
        self.time+=1


    def getNewsFeed(self, userId: int) -> List[int]:
        all_followers = self.follows[userId].copy()
        all_followers.add(userId)

        heap = []
        for follower in all_followers:
            for time, postId in self.posts[follower]:
                heapq.heappush(heap,(-time, postId))

        res = []
        while heap and len(res) < 10:
            res.append(heapq.heappop(heap)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
