import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(current_date)
    
    def calculate_future_date():
            num_of_days = int(input("Enter number of days:"))
            future_date = current_date + timedelta(days=num_of_days)
            print(future_date)
