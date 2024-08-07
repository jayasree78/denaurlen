class User:
    def __init__(self, username, followers, u_coins):
        self.username = username
        self.followers = followers
        self.u_coins = u_coins
        self.is_verified = False

    def verify_user(self):
        if self.followers > 200000 and self.u_coins > 200000:
            self.is_verified = True
        return self.is_verified

# Example Usage
username = input("Enter username: ")
followers = int(input("Enter number of followers: "))
u_coins = int(input("Enter amount of U coins: "))

user = User(username, followers, u_coins)

if user.verify_user():
    print(f"User {user.username} is verified.")
else:
    print(f"User {user.username} does not meet the verification criteria.")
