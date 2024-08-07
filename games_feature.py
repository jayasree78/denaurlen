import random

class User:
    def __init__(self, username, u_coins):
        self.username = username
        self.u_coins = u_coins
        self.correct_labels = 0

    def __str__(self):
        return f"{self.username} - U coins: {self.u_coins}, Correct Labels: {self.correct_labels}"

def get_user_input():
    username = input("Enter username: ")
    u_coins = int(input("Enter amount of U coins: "))
    return User(username, u_coins)

def play_labeling_game(users):
    objects = ["Dog", "Cat", "Apple", "Car", "Book"]
    incorrect_labels = ["Fruit", "Vehicle", "Animal", "Gadget", "Plant"]
    object_label_pairs = list(zip(objects, incorrect_labels))

    print("\nStarting the labeling game...")
    
    for user in users:
        print(f"\n{user.username}'s turn to label:")
        random.shuffle(object_label_pairs)
        user.correct_labels = 0

        for obj, incorrect_label in object_label_pairs:
            print(f"Object: {obj}, Incorrect Label: {incorrect_label}")
            correct_label = input("Enter the correct label: ")

            if correct_label.lower() == obj.lower():
                user.correct_labels += 1
                print("Correct!")
            else:
                print(f"Wrong! The correct label is {obj}.")

    # Determine the winner and distribute rewards
    max_correct = max(user.correct_labels for user in users)
    winners = [user for user in users if user.correct_labels == max_correct]

    if len(winners) == 1:
        winner = winners[0]
        loser_penalty = 5000  # Example penalty for losing
        reward = loser_penalty * (len(users) - 1)
        print(f"\nThe winner is {winner.username} with {winner.correct_labels} correct labels!")
        
        for user in users:
            if user != winner:
                user.u_coins -= loser_penalty
                winner.u_coins += loser_penalty // 5  # Distribute 1/5th of the penalty to the winner

        winner.u_coins += reward
        print(f"{winner.username} wins {reward} U coins!")

    else:
        print("\nIt's a tie! No rewards distributed.")

    print("\nFinal standings:")
    for user in users:
        print(user)

# Example Usage
users = []
num_users = int(input("Enter the number of users (4 or 5): "))

for _ in range(num_users):
    users.append(get_user_input())

play_labeling_game(users)
