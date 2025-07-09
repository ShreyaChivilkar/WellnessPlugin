from datetime import datetime, time, timedelta
import random
import requests

WELLNESS_MESSAGES = {
    "morning": {
        "short": [
            "💧 Grab a glass of water to refresh.",
            "🙆‍♂️ Do a quick stretch at your desk.",
            "🧘‍♀️ Take 5 deep breaths — relax before the next meeting."
        ],
        "medium": [
            "🚶‍♂️ Walk around your floor or to the pantry.",
            "🍵 Make yourself a cup of tea or coffee.",
            "👀 Try the 20-20-20 rule: every 20 mins, look 20 ft away for 20 secs."
        ],
        "long": [
            "🚶‍♀️ Go for a walk around the building or outside if safe.",
            "📓 Jot down your thoughts or plan the rest of your day.",
            "🤸 Do a quick desk yoga session in a quiet space."
        ]
    },
    "afternoon": {
        "short": [
            "💦 Time to hydrate — refill your water bottle.",
            "🙆‍♀️ Roll your shoulders and take a breath.",
            "🧍‍♂️ Stand up, adjust your posture, and look away from your screen."
        ],
        "medium": [
            "🍽️ Grab a healthy snack and unwind for a bit.",
            "🧍‍♀️ Take a slow walk to reset your focus.",
            "📖 Read a short article or fun fact unrelated to work."
        ],
        "long": [
            "🧘 Find a quiet corner and do a short mindfulness exercise.",
            "🏃‍♂️ Take a brisk indoor walk or climb some stairs.",
            "🤝 Chat casually with a coworker to refresh your mind."
        ]
    },
    "evening": {
        "short": [
            "🚰 Drink water before wrapping up the day.",
            "🪟 Look outside and rest your eyes.",
            "🙆 Stretch your arms and take a few deep breaths."
        ],
        "medium": [
            "🌿 Step away from your desk and do nothing — yes, really.",
            "📱Call or message a loved one for a quick chat.",
            "🎶 Listen to a calming track to destress."
        ],
        "long": [
            "🧘 Practice light meditation or breathing in a quiet area.",
            "📝 Reflect on what went well today.",
            "🚶‍♀️ Take a walk and prepare your mind for winding down."
        ]
    }
}

def get_time_of_day(dt: datetime) -> str:
    if dt.time() < time(12, 0):
        return "morning"
    elif dt.time() < time(17, 0):
        return "afternoon"
    else:
        return "evening"

def get_duration_bucket(start: datetime, end: datetime) -> str:
    duration = end - start
    if duration <= timedelta(minutes=5):
        return "short"
    elif duration <= timedelta(minutes=20):
        return "medium"
    else:
        return "long"

def get_quote_of_the_day(api_key=None):
    """
    Fetches the quote of the day from ZenQuotes API and returns the 'q' (quote) part.
    :param api_key: (optional) Your ZenQuotes API key as a string.
    :return: Quote of the day as a string, or None if failed.
    """
    url = f'https://zenquotes.io/api/today/{api_key}' if api_key else 'https://zenquotes.io/api/today'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data[0]['q']
    except Exception as e:
        print("Error fetching quote:", e)
        return None

def pick_wellness_message(slot_start: datetime, slot_end: datetime) -> str:
    tod = get_time_of_day(slot_start)
    duration_bucket = get_duration_bucket(slot_start, slot_end)
    messages = WELLNESS_MESSAGES.get(tod, {}).get(duration_bucket, [])
    if not messages:
        return "Take a short break and recharge!"  # Fallback message
    return random.choice(messages)

def find_free_slots(events, work_start=time(8,0), work_end=time(22,0)):
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