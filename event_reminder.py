import time
from plyer import notification

def event_notification():
    #if __name__ == "__main__":
        notification.notify(
        title = "Event Alert",
        message = " KJSCE's Annual Function is about to start. You defenitely dont want to miss out some crazy stuff that's going to happen today."
                "Join now immediately.",
        app_icon = "event.ico",
        timeout = 15
        )

def snooze():
    choice = 0
    while choice !="No":
        choice = input("Do you want me to remind you after 5 Mins.Type Yes to continue No to stop: ")
        time.sleep(5*60)
        event_notification()
        

