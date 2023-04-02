from plyer import notification
import time

# define the notification message
title = "Reminder"
message = "one Hour has passed, remember to take breaks from your computer"

# define the duration between notifications (in seconds)
interval = 3600  # 1 hour

while True:
    # display the notification
    notification.notify(
        title=title,
        message=message,
        timeout=10  # display for 10 seconds
    )

    # wait for the specified interval before displaying the next notification
    time.sleep(interval)
