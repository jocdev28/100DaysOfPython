# Creating a class
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1

class Car:
    def __init__(self, seats):
        self.seats = seats

    def enter_race_mode(self):
        self.seats = 2



user1 = User("001", "Angela")
user2 = User("002", "Michael")
print(user1.id, user1.username)

user2.follow(user1)
print(user1.following, user1.followers)
print(user2.following, user2.followers)
# Adding attributes to a class
user1.id = "001"
user1.name = "Fisher"

car = Car(5)
print(car.seats)

car.enter_race_mode()
print(car.seats)



