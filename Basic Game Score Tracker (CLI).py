class GameScoreTracker:
    def __init__(self):
        self.scores = {}

    def add_player(self, name):
        if name in self.scores:
            print(f"Player '{name}' already exists!")
        else:
            self.scores[name] = 0
            print(f"Player '{name}' added.")

    def update_score(self, name, points):
        if name in self.scores:
            self.scores[name] += points
            print(f"Updated {name}'s score by {points}. New score: {self.scores[name]}")
        else:
            print(f"Player '{name}' does not exist!")

    def view_scores(self):
        if self.scores:
            print("\nCurrent Scores:")
            for player, score in self.scores.items():
                print(f"{player}: {score}")
        else:
            print("No players to display.")

    def reset_scores(self):
        
        self.scores = {}
        print("All scores have been reset.")

    def run(self):
        while True:
            print("\n Basic Game Score Tracker ")
            print("1. Add Player")
            print("2. Update Score")
            print("3. View Scores")
            print("4. Reset Scores")
            print("5. Exit")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                name = input("Enter player's name: ").strip()
                self.add_player(name)
            elif choice == "2":
                name = input("Enter player's name: ").strip()
                try:
                    points = int(input("Enter points to add or subtract: ").strip())
                    self.update_score(name, points)
                except ValueError:
                    print("Invalid points value. Please enter an integer.")
            elif choice == "3":
                self.view_scores()
            elif choice == "4":
                self.reset_scores()
            elif choice == "5":
                print("Exiting the game score tracker.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    tracker = GameScoreTracker()
    tracker.run()
