from datetime import datetime

def display_current_date():
    current_date = datetime.now().date()
    print(f"Current Date: {current_date}")

display_current_date()
