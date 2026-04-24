# main.py

from scheduler import generate_block, DAYS
from rich.console import Console
from rich.table import Table

console = Console()


def get_rating(prompt):
    while True:
        try:
            val = int(input(prompt))
            if 1 <= val <= 5:
                return val
            print("Whoops! Enter 1–5.")
        except:
            print("Invalid input.")


def get_int(prompt, min_v, max_v):
    while True:
        try:
            val = int(input(prompt))
            if min_v <= val <= max_v:
                return val
            print(f"Enter {min_v}-{max_v}")
        except:
            print("Invalid input.")
def get_goal():
    while True:
        choice = input("Enter 1, 2, or 3: ").strip()

        if choice in ["1", "2", "3"]:
            return choice

        print("Whoops! Please enter 1, 2, or 3.")

def main():
    print("Welcome to Squash Training Planner\n")

    name = input("Enter your name: ")

    print(f"\nAlright {name}, let’s build your plan.\n")

    # PHYSICAL
    print("Rate physical abilities (1–5)\n")
    physical = {
        "speed": get_rating("Speed: "),
        "endurance": get_rating("Endurance: "),
        "strength": get_rating("Strength: "),
        "explosiveness": get_rating("Explosiveness: "),
        "injury_prevention": get_rating("Injury Prevention: ")
    }

    # SQUASH
    print("\nRate squash skills\n")
    squash = {
        "front_court": get_rating("Front court: "),
        "back_court": get_rating("Back court: "),
        "movement": get_rating("Movement: "),
        "tactics": get_rating("Tactics: "),
        "consistency": get_rating("Consistency: ")
    }

    # MENTAL
    print("\nRate mental game\n")
    mental = {
        "focus": get_rating("Focus: "),
        "confidence": get_rating("Confidence: "),
        "composure": get_rating("Composure: "),
        "decision_making": get_rating("Decision making: "),
        "resilience": get_rating("Resilience: ")
    }

    # GOAL
    print("\nChoose goal:")
    print("1. Improve weaknesses")
    print("2. Balanced training")
    print("3. Competition prep")

    goal = get_goal()

    # REST DAYS INPUT
    print("\nHow many rest days will you take?")
    rest_count = get_int("Enter number of rest days (0–6): ", 0, 6)

    print("\nEnter your rest days (e.g. Monday):")

    rest_days = []
    while len(rest_days) < rest_count:
        day = input(f"Rest day {len(rest_days)+1}: ").strip().capitalize()

        if day not in DAYS:
            print("Invalid day. Try again.")
        elif day in rest_days:
            print("You already entered that day.")
        else:
            rest_days.append(day)

    weeks = get_int("\nWeeks (max 8 recommended): ", 1, 8)

    plan = generate_block(weeks, physical, squash, mental, goal, rest_days)

    # OUTPUT
    for week, data in plan.items():
        console.print(f"\n[bold cyan]{week}[/bold cyan]")

        table = Table()
        table.add_column("Day")
        table.add_column("Type")
        table.add_column("Morning")
        table.add_column("Afternoon")
        table.add_column("Evening")

        for day, (stype, sessions) in data.items():
            table.add_row(
                day,
                stype,
                sessions["Morning"],
                sessions["Afternoon"],
                sessions["Evening"]
            )

        console.print(table)


if __name__ == "__main__":
    main()