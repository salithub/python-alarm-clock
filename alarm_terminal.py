import time
from datetime import datetime

alarm_time = input("Enter alarm time (HH:MM): ").strip()

print("Alarm set...")

while True:
    current_time = datetime.now().strftime("%H:%M")

    if current_time == alarm_time:
        print("⏰ WAKE UP! ⏰")
        break

    time.sleep(1)