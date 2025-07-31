# Scripting - Simple set of executable instructions

from dotenv import load_dotenv
import os
from garminconnect import Garmin, GarminConnectAuthenticationError

# Load the .env file
load_dotenv()

email = os.getenv("GC_EMAIL")
password = os.getenv("GC_PASSWORD")

def get_last_activity():
    try:
        client = Garmin(email, password)
        client.login()
        # Get activity info
        activity = client.get_last_activity()

        # Selected fields
        activity_data = (
            f"Activity Name: {activity.get('activityName')}\n"
            f"Start Time: {activity.get('startTimeLocal', 'N/A')}\n"
            f"Distance (km): {activity.get('distance')}\n"
            f"Duration (min): {activity.get('duration')}\n"
            f"Calories: {activity.get('calories')}\n"
            f"Average Heart Rate: {activity.get('averageHR')}\n"
        )

        print(activity_data)

    except GarminConnectAuthenticationError:
        print("Authentication error")

get_last_activity()