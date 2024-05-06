from datetime import datetime

def minutes_lived_since_birth(birthdate):
    
    birth_date_obj = datetime.strptime(birthdate, "%d/%m/%Y")


    time_lived = datetime.now() - birth_date_obj


    total_minutes_lived = int(time_lived.total_seconds() / 60)

    
    print(f"You have lived approximately {total_minutes_lived} minutes in your life.")


birthdate = "17/08/1999"
minutes_lived_since_birth(birthdate)
