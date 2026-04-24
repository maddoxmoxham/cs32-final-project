# scheduler.py

import random
from workouts import fitness_workouts, squash_drills, mental_training

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
TIMES = ["Morning", "Afternoon", "Evening"]


def get_weaknesses(ratings):
    return sorted(ratings, key=ratings.get)


def weighted_choice(weaknesses):
    weakest = weaknesses[0]
    second = weaknesses[1] if len(weaknesses) > 1 else weakest
    third = weaknesses[2] if len(weaknesses) > 2 else second
    return [weakest]*6 + [second]*3 + [third]*1


def pick_with_no_streak(pool, history):
    if len(history) >= 2 and history[-1] == history[-2]:
        blocked = history[-1]
        filtered = [x for x in pool if x != blocked]
        if filtered:
            return random.choice(filtered)
    return random.choice(pool)


def pick_from_category(category, type_):
    if type_ == "fitness":
        return random.choice(fitness_workouts[category])
    elif type_ == "squash":
        return random.choice(squash_drills[category])
    elif type_ == "mental":
        return random.choice(mental_training[category])


def get_session_type(day_index):
    if day_index % 4 == 3:
        return "Recovery"
    elif day_index % 3 == 0:
        return "Conditioning"
    elif day_index % 3 == 1:
        return "Technical"
    else:
        return "Match"


def generate_day(day_index, phys_pool, squash_pool, mental_pool,
                 phys_hist, squash_hist, mental_hist, goal):

    session_type = get_session_type(day_index)

    # ---------------------------
    # RECOVERY DAY
    # ---------------------------
    if session_type == "Recovery":
        return session_type, [
            pick_from_category("injury_prevention", "fitness"),
            pick_from_category("consistency", "squash"),
            pick_from_category("resilience", "mental")
        ]

    # ---------------------------
    # DETERMINE SQUASH FOCUS BY DAY TYPE
    # ---------------------------
    if session_type == "Match":
        squash_category = "tactics"

    elif session_type == "Technical":
        squash_category = "front_court"

    elif session_type == "Conditioning":
        squash_category = "movement"  # or back_court mix

    else:
        squash_category = "consistency"

    # ---------------------------
    # PICK FITNESS + MENTAL (UNCHANGED LOGIC)
    # ---------------------------
    phys = pick_with_no_streak(phys_pool, phys_hist)
    mental = pick_with_no_streak(mental_pool, mental_hist)

    phys_hist.append(phys)
    mental_hist.append(mental)

    phys_hist[:] = phys_hist[-2:]
    mental_hist[:] = mental_hist[-2:]

    # ---------------------------
    # BUILD FINAL DAY
    # ---------------------------
    return session_type, [
        pick_from_category(phys, "fitness"),
        pick_from_category(squash_category, "squash"),
        pick_from_category(mental, "mental")
    ]

def generate_week(phys_w, squash_w, mental_w, goal, rest_days):

    phys_pool = weighted_choice(phys_w)
    squash_pool = weighted_choice(squash_w)
    mental_pool = weighted_choice(mental_w)

    phys_hist, squash_hist, mental_hist = [], [], []

    week = {}
    training_index = 0

    for day in DAYS:

        # USER-DEFINED REST DAY
        if day in rest_days:
            week[day] = ("Rest", {
                "Morning": "Rest",
                "Afternoon": "Rest",
                "Evening": "Rest"
            })
            continue

        session_type, activities = generate_day(
            training_index,
            phys_pool, squash_pool, mental_pool,
            phys_hist, squash_hist, mental_hist,
            goal
        )

        schedule = {
            "Morning": activities[0],
            "Afternoon": activities[1],
            "Evening": activities[2]
        }

        week[day] = (session_type, schedule)

        training_index += 1

    return week


def generate_block(weeks, phys, squash, mental, goal, rest_days):

    phys_w = get_weaknesses(phys)
    squash_w = get_weaknesses(squash)
    mental_w = get_weaknesses(mental)

    block = {}

    for w in range(weeks):
        block[f"Week {w+1}"] = generate_week(
            phys_w, squash_w, mental_w, goal, rest_days
        )

    return block