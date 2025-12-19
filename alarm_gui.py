import time
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import messagebox
import threading
import winsound

# List to store multiple alarms
alarms = []

# -------------------- ALARM FUNCTIONS --------------------
def alarm_popup(alarm_time):
    popup = tk.Toplevel(root)
    popup.title("ALARM")
    popup.geometry("250x150")
    popup.configure(bg="red")

    label = tk.Label(popup, text=f"⏰ WAKE UP! {alarm_time}", font=("Helvetica", 14), bg="red", fg="white")
    label.pack(pady=15)

    # Function to stop alarm
    def stop_alarm():
        popup.destroy()

    # Function to snooze alarm by 5 minutes
    def snooze_alarm():
        popup.destroy()
        new_time = (datetime.strptime(alarm_time, "%H:%M") + timedelta(minutes=5)).strftime("%H:%M")
        alarms.append(new_time)
        messagebox.showinfo("Snooze", f"Alarm snoozed to {new_time}")

    stop_btn = tk.Button(popup, text="Stop", command=stop_alarm)
    stop_btn.pack(side="left", padx=20, pady=10)

    snooze_btn = tk.Button(popup, text="Snooze 5 min", command=snooze_alarm)
    snooze_btn.pack(side="right", padx=20, pady=10)

    # Play sound continuously
    def play_sound():
        for _ in range(10):
            winsound.Beep(1000, 1000)
    threading.Thread(target=play_sound).start()


def check_alarms():
    while True:
        now = datetime.now().strftime("%H:%M")
        for alarm_time in alarms.copy():
            if now == alarm_time:
                alarms.remove(alarm_time)  # Remove from list so it doesn't repeat
                alarm_popup(alarm_time)
        time.sleep(1)

def set_alarm():
    alarm_time = entry.get().strip()
    if alarm_time:
        alarms.append(alarm_time)
        messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")
        entry.delete(0, tk.END)

# -------------------- GUI SETUP --------------------
root = tk.Tk()
root.title("Advanced Alarm Clock")
root.geometry("350x200")

# Label
label = tk.Label(root, text="Enter alarm time (HH:MM, 24-hour format):")
label.pack(pady=10)

# Entry box
entry = tk.Entry(root)
entry.pack(pady=5)

# Set Alarm button
button = tk.Button(root, text="Set Alarm", command=set_alarm)
button.pack(pady=10)

# Start checking alarms in a separate thread
threading.Thread(target=check_alarms, daemon=True).start()

root.mainloop()