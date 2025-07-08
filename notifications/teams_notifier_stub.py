import requests

def send_notification(slot, message):
    url = "http://your-endpoint.example.com/notify" 
    payload = {
        "start": slot[0].isoformat(),
        "end": slot[1].isoformat(),
        "message": message
    }
    try:
        response = requests.post(url, json=payload)
        print(f"Notification sent, status: {response.status_code}, response: {response.text}")
    except Exception as e:
        print(f"Failed to send notification: {e}")