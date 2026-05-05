# main.py
import csv
from scheduler import generate_block, DAYS
from rich.console import Console
from rich.table import Table

console = Console()

#rating skill strength
def get_rating(prompt):
    while True:
        try:
            val = int(input(prompt))
            if 1 <= val <= 5:
                return val
            print("Whoops! Enter 1–5.")
        except:
            print("Invalid input.")

#retriever and store rating
def get_int(prompt, min_v, max_v):
    while True:
        try:
            val = int(input(prompt))
            if min_v <= val <= max_v:
                return val
            print(f"Enter {min_v}-{max_v}")
        except:
            print("Invalid input.")
#choosing specfici plan goal
def get_goal():
    while True:
        choice = input("Enter 1, 2, or 3: ").strip()

        if choice in ["1", "2", "3"]:
            return choice

        print("Whoops! Please enter 1, 2, or 3.")


#export to csv for excel or sheets use
def export_to_csv(plan, filename="training_plan.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Week", "Day", "Type", "Morning", "Afternoon", "Evening", "Nutrition"])

        for week, days in plan.items():
            for day, (stype, sessions) in days.items():
                writer.writerow([
                    week,
                    day,
                    stype,
                    sessions["Morning"],
                    sessions["Afternoon"],
                    sessions["Evening"],
                    sessions["Nutrition"]
                ])
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
    #cycle through asking for which days are restdays untill equal to inputted number
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

    # Table format output
    for week, days in plan.items():
        table = Table(title=week)

        # Columns
        table.add_column("Day", style="bold")
        table.add_column("Type")
        table.add_column("Morning")
        table.add_column("Afternoon")
        table.add_column("Evening")
        table.add_column("Nutrition")

        for day, (stype, sessions) in days.items():
            table.add_row(
                day,
                stype,
                sessions["Morning"],
                sessions["Afternoon"],
                sessions["Evening"],
                sessions["Nutrition"]
            )

        console.print(table)  # ✅ moved OUTSIDE loop

    export_to_csv(plan)
    print(f"\n{name}, your training plan has been saved as training_plan.csv!")
if __name__ == "__main__":
    main()