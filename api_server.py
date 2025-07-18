from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
from mycalendar.dummy_calendar import get_events_for_today
from wellness import find_free_slots, pick_wellness_message
from notifications.teams_notifier_stub import send_notification
from wellness import get_quote_of_the_day
from datetime import datetime, time

app = Flask(__name__)
CORS(app)

notified_slots = set()
last_quote_sent_date = None

@app.route('/notify', methods=['GET'])
def notify():
    # Optional query parameters
    start = request.args.get('start')
    end = request.args.get('end')
    message = request.args.get('message')

    global last_quote_sent_date
    now = datetime.now()
    today = now.date()
    if now.time() < time(12, 0) and last_quote_sent_date != today:
        quote = get_quote_of_the_day()
        if quote:
            print("insideee")
            slot = (now, now)
            send_notification(slot, f"🌞 Quote of the Day:\n{quote}")
            last_quote_sent_date = today
            return jsonify({
                "status": "Quote notification sent",
                "date": today.isoformat(),
                "slot_start": slot[0].isoformat(),
                "slot_end": slot[1].isoformat(),
                "msg": quote
            })
    elif start and end:
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

    msg = message if message else pick_wellness_message(slot[0], slot[1])
    send_notification(slot, msg)
    return jsonify({
        "status": "Notification sent",
        "slot_start": slot[0].isoformat(),
        "slot_end": slot[1].isoformat(),
        "message": msg
    })

if __name__ == "__main__":
    app.run(port=5000)