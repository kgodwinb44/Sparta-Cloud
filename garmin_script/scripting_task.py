# Scripting - Simple set of executable instructions

from dotenv import load_dotenv
import os
from garminconnect import Garmin, GarminConnectAuthenticationError

# Load the .env file
load_dotenv()

email = os.getenv("GC_EMAIL")
password = os.getenv("GC_PASSWORD")

try:
    client = Garmin(email, password)
    client.login()

    # Get activity info
    activity = client.get_last_activity()

    # Print selected fields
    print("\n")
    print(f"Activity Name: {activity.get('activityName')}")
    print(f"Start Time: {activity.get('startTimeLocal', 'N/A')}")
    print(f"Distance (km): {activity.get('distance') / 1000:.2f}")
    print(f"Duration (min): {activity.get('duration') / 60:.2f}")
    print(f"Calories: {activity.get('calories')}")
    print(f"Average Heart Rate: {activity.get('averageHR')}")

except GarminConnectAuthenticationError:
    print("Authentication error")