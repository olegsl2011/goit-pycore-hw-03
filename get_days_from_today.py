from datetime import datetime 

def get_days_from_today(date):
    try: 
        year, month, day = date.split("-")
        formatedDate = datetime(year=int(year), month=int(month), day=int(day))
        dateNow = datetime.now().date()
        return  formatedDate.toordinal() - dateNow.toordinal()
    except ValueError: 
        print(f"{date} is not a YYYY-MM-DD date")



print(get_days_from_today("NOTDATE"))
print(get_days_from_today("2024-06-12"))