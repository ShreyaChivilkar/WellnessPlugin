from datetime import datetime, time, timedelta
import random

WELLNESS_MESSAGES = [
    "💧 Drink some water!",
    "🚶 Take a short walk to refresh your mind.",
    "☕ How about a coffee break?",
    "👀 Rest your eyes for a few minutes.",
    "🧘 Try a quick breathing exercise.",
]

def pick_wellness_message():
    return random.choice(WELLNESS_MESSAGES)

def find_free_slots(events, work_start=time(9,0), work_end=time(17,0)):
    if not events:
        # No events, whole workday is free
        today = datetime.now().date()
        return [(datetime.combine(today, work_start), datetime.combine(today, work_end))]

    events = sorted(events, key=lambda e: e["start"])
    free_slots = []
    current = datetime.combine(events[0]["start"].date(), work_start)

    for event in events:
        if event["start"] > current:
            free_slots.append((current, event["start"]))
        current = max(current, event["end"])

    workday_end = datetime.combine(events[0]["start"].date(), work_end)
    if current < workday_end:
        free_slots.append((current, workday_end))
    return free_slots


def should_notify_now(slot, lead_time_minutes=5):
    now = datetime.now()
    notify_time = slot[0] - timedelta(minutes=lead_time_minutes)
    return notify_time <= now < slot[1]