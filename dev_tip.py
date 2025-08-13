import random


tips = [
    "Use 'git status' often to see your repo state.",
    "Commit small, focused changes with clear messages.",
    "Learn to use 'git rebase -i' for clean history.",
    "Practice reading error logs before Googling.",
    "Automate repetitive tasks with scripts or Makefiles.",
    "Keep your terminal organized with aliases.",
    "Use virtual environments for Python projects.",
    "Regularly pull and merge changes from main branch.",
    "Write descriptive variable and function names.",
    "Use code comments to explain 'why', not 'what'.",
    "Learn keyboard shortcuts for your IDE or editor.",
    "Set up proper logging instead of using print statements.",
    "Use linters and formatters to maintain code quality.",
    "Practice Test-Driven Development (TDD) for better code.",
    "Keep functions small and focused on a single task.",
    "Use environment variables for configuration settings.",
    "Back up your work frequently, not just with git.",
    "Learn to use debuggers instead of printf debugging.",
    "Read documentation thoroughly before asking for help.",
    "Use meaningful git branch names that describe features.",
    "Set up continuous integration for your projects.",
    "Learn regular expressions for text processing tasks.",
    "Use package managers properly and lock dependency versions."
]


def main():
    print("🛠️  Dev Tip of the Day:")
    print(random.choice(tips))


if __name__ == "__main__":
    main()
