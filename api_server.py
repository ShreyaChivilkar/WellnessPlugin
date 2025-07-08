from flask import Flask, request, jsonify
from datetime import datetime
from mycalendar.dummy_calendar import get_events_for_today
from wellness import find_free_slots, pick_wellness_message
from notifications.teams_notifier_stub import send_notification

app = Flask(__name__)
notified_slots = set()

@app.route('/notify', methods=['GET'])
def notify():
    # Optional query parameters
    start = request.args.get('start')
    end = request.args.get('end')
    message = request.args.get('message')

    if start and end:
        try:
            slot = (datetime.fromisoformat(start), datetime.fromisoformat(end))
        except Exception as e:
            return jsonify({"error": "Invalid datetime format"}), 400
    else:
        # Find next free slot
        events = get_events_for_today()
        free_slots = find_free_slots(events)
        now = datetime.now()
        slot = None
        for s in free_slots:
            if s[1] > now:  # Slot is ongoing or upcoming
                slot_key = (s[0].isoformat(), s[1].isoformat())
                if slot_key not in notified_slots:
                    slot = s
                    break
        if not slot:
            return jsonify({"error": "No upcoming free slot found or all notified."}), 404

        # Mark this slot as notified
        slot_key = (slot[0].isoformat(), slot[1].isoformat())
        notified_slots.add(slot_key)

    msg = message if message else pick_wellness_message()
    send_notification(slot, msg)
    return jsonify({
        "status": "Notification sent",
        "slot_start": slot[0].isoformat(),
        "slot_end": slot[1].isoformat(),
        "message": msg
    })

if __name__ == "__main__":
    app.run(port=5000)