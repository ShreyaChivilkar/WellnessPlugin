from datetime import datetime

def get_events_for_today():
    # Dummy events for today (update the date if testing on a different day)
     return [
        {"start": datetime(2025, 7, 8, 9, 0), "end": datetime(2025, 7, 8, 10, 0)},
        {"start": datetime(2025, 7, 8, 11, 0), "end": datetime(2025, 7, 8, 11, 27)},
        {"start": datetime(2025, 7, 8, 14, 0), "end": datetime(2025, 7, 8, 15, 0)},
    ]