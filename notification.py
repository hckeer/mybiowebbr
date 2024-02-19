from win10toast import ToastNotifier
import time

while True:
    toaster = ToastNotifier()
    toaster.show_toast("Water Notification", "Nowadays you are not drinking enough water", icon_path="aaaaaaaa.jpg", duration=5)
    while toaster.notification_active(): 
        time.sleep(0.1)

    time.sleep(1800)
