import random


tips = [
    "Use 'git status' often to see your repo state.",
    "Commit small, focused changes with clear messages.",
    "Learn to use 'git rebase -i' for clean history.",
    "Practice reading error logs before Googling.",
    "Automate repetitive tasks with scripts or Makefiles.",
    "Keep your terminal organized with aliases.",
    "Use virtual environments for Python projects.",
    "Regularly pull and merge changes from main branch."
]


def main():
    print("🛠️  Dev Tip of the Day:")
    print(random.choice(tips))


if __name__ == "__main__":
    main()
