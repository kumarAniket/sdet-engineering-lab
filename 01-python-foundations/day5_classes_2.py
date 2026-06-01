class User:
    def __init__(self,user_id,username):
        self.id=user_id
        self.username=username
        self.followers=0
        self.following=0

    def follow(self,user):
        user.followers+=1
        self.following+=1

user_1 = User("001","aniket")
user_2 = User("002","kumar")

user_1.follow(user_2)

print(user_1.id + " belongs to " + user_1.username + " with " + str(user_1.following) + " following count")
print(user_2.id + " belongs to " + user_2.username + " with " + str(user_2.followers) + " follower count")
