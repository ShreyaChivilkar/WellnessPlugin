# import time
# from datetime import datetime
# from calendar.dummy_calendar import get_events_for_today
# from wellness import find_free_slots, pick_wellness_message, should_notify_now
# from notifications.teams_notifier_stub import send_notification

# def slot_to_str(slot):
#     # Unique identifier for a slot
#     return f"{slot[0].isoformat()}_{slot[1].isoformat()}"

# def main():
#     events = get_events_for_today()
#     free_slots = find_free_slots(events)
#     notified_slots = set()

#     while True:
#         for slot in free_slots:
#             slot_id = slot_to_str(slot)
#             if slot_id in notified_slots:
#                 continue
#             if should_notify_now(slot):
#                 message = pick_wellness_message()
#                 send_notification(slot, message)
#                 notified_slots.add(slot_id)
#         time.sleep(60)  # Check every minute

# if __name__ == "__main__":
#     main()