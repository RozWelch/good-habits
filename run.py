# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT =  gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('habit_tracker')
# link to Google sheet dailyhabits worksheet
habits = SHEET.worksheet('dailyhabits')
data = habits.get_all_values()

print("Welcome to the daily good habits tracker!")
# user inputs name and daily excercise / diet data
name = input("Please enter your name\n")
stretch_time = input(f"Hello {name}, please enter your minutes spent streching today: ")
walk_dog_time = input(f"Enter your time minutes walking the dog today: ")
gym_time = input(f"Enter your time minutes at the gym today: ")
veg_portion = input(f"Enter how many portions of veg you ate today: ")
glasses_water = input(f"Enter how many glasses of water your drank today: ")
green_tea = input(f"Enter how many cups of green tea you drank (instead of the usual tea/coffee!): ")
