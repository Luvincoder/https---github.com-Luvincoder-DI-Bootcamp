from datetime import datetime

def time_until_january_first():

    current_date = datetime.now()

   
    january_first_next_year = datetime(current_date.year + 1, 1, 1)

    
    time_left = january_first_next_year - current_date

   
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    
    print(f"The 1st of January is in {days} days and {hours:02}:{minutes:02}:{seconds:02} hours.")


time_until_january_first()
