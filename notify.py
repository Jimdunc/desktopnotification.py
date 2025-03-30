from plyer import notification

# Send notification
notification.notify(
    title="Hello, James!",
    message="WELCOME TO YOUR DESKTOP!",
    app_name="Python Notifier",
    timeout=10  # Notification disappears after 10 seconds
)
