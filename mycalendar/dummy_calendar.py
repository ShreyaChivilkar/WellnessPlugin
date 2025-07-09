from datetime import datetime

def get_events_for_today():
    # Updated events for July 8, 2025
    return [
        {"start": datetime(2025, 7, 8, 9, 0), "end": datetime(2025, 7, 8, 10, 0)},
        {"start": datetime(2025, 7, 8, 9, 30), "end": datetime(2025, 7, 8, 9, 45)},   # Standup
        {"start": datetime(2025, 7, 8, 9, 50), "end": datetime(2025, 7, 8, 10, 0)},    # Standup
        {"start": datetime(2025, 7, 8, 11, 0), "end": datetime(2025, 7, 8, 11, 27)},
        {"start": datetime(2025, 7, 8, 11, 15), "end": datetime(2025, 7, 8, 12, 15)},  # Meeting
        {"start": datetime(2025, 7, 8, 13, 45), "end": datetime(2025, 7, 8, 14, 0)},   # Meeting
        {"start": datetime(2025, 7, 8, 14, 0), "end": datetime(2025, 7, 8, 15, 0)},
        {"start": datetime(2025, 7, 8, 14, 15), "end": datetime(2025, 7, 8, 15, 0)},   # Meeting
        {"start": datetime(2025, 7, 8, 15, 30), "end": datetime(2025, 7, 8, 16, 15)},  # Meeting
        {"start": datetime(2025, 7, 8, 17, 0), "end": datetime(2025, 7, 8, 18, 0)},    # Meet
        {"start": datetime(2025, 7, 8, 19, 0), "end": datetime(2025, 7, 8, 20, 42)},
        {"start": datetime(2025, 7, 8, 20, 55), "end": datetime(2025, 7, 8, 21, 42)},

        {"start": datetime(2025, 7, 9, 9, 0), "end": datetime(2025, 7, 9, 10, 0)},
        {"start": datetime(2025, 7, 9, 9, 30), "end": datetime(2025, 7, 9, 9, 45)},   # Standup
        {"start": datetime(2025, 7, 9, 9, 50), "end": datetime(2025, 7, 9, 10, 0)},    # Standup
        {"start": datetime(2025, 7, 9, 11, 0), "end": datetime(2025, 7, 9, 11, 27)},
        {"start": datetime(2025, 7, 9, 11, 15), "end": datetime(2025, 7, 9, 12, 15)},  # Meeting
        {"start": datetime(2025, 7, 9, 13, 45), "end": datetime(2025, 7, 9, 14, 0)},   # Meeting
        {"start": datetime(2025, 7, 9, 14, 0), "end": datetime(2025, 7, 9, 15, 0)},
        {"start": datetime(2025, 7, 9, 14, 15), "end": datetime(2025, 7, 9, 15, 0)},   # Meeting
        {"start": datetime(2025, 7, 9, 15, 30), "end": datetime(2025, 7, 9, 16, 15)},  # Meeting
        {"start": datetime(2025, 7, 9, 17, 0), "end": datetime(2025, 7, 9, 18, 0)},    # Meet
        {"start": datetime(2025, 7, 9, 19, 0), "end": datetime(2025, 7, 9, 20, 42)},
        {"start": datetime(2025, 7, 9, 20, 55), "end": datetime(2025, 7, 9, 21, 42)}
    ]