class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user):
        self.following += 1  # The user who we want to follow account goes up by 1
        user.follower += 1  # My follower goes up by 1


user_1 = User("001", "SG")
user_2 = User("002", "Jona")
user_2.follow(user_1)
print(user_1.follower)
print(user_2.following)

