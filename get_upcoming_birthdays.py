from datetime import datetime, timedelta
import calendar


def get_upcoming_birthdays(users):
    result = []
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d")
        happyDay = isCongratulate(birthday)
        if happyDay:
            congratulateDate = skipHolidays(happyDay)
            result.append({"name": user["name"], "congratulation_date": congratulateDate.strftime("%Y.%m.%d")})
    return result

def isCongratulate(date: datetime):
    now = datetime.now().date().toordinal()
    thisYear = closestBirthday(date).toordinal()
    nextYear = closestBirthday(date, True).toordinal()
    if 7 > thisYear - now and thisYear - now >= 0: 
        return closestBirthday(date)
    elif 7 > nextYear - now and nextYear - now >= 0: 
        return closestBirthday(date, True)
    else: 
        return False



def closestBirthday(realDate: datetime, nextYear: bool=False) -> datetime:
    desiredYear = datetime.now().year + 1 if nextYear else datetime.now().year
    if realDate.month != 2 or realDate.day != 29:
        return datetime(year=desiredYear, month=realDate.month, day=realDate.day)
    else: 
        if calendar.isleap(desiredYear):
            return datetime(year=desiredYear, month=realDate.month, day=realDate.day)
        else: 
            return datetime(year=desiredYear, month=3, day=1)
        
def skipHolidays(date: datetime): 
    result = date
    if date.weekday() == 6:
        result = result + timedelta(days=1)
    elif date.weekday() == 5:
        result = result + timedelta(days=2)
    return result
    


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Jane Smith", "birthday": "2020.02.29"},
    {"name": "April First", "birthday": "2020.04.01"},
    {"name": "April Second", "birthday": "2020.04.02"},
    {"name": "April Fifth", "birthday": "2020.04.05"},
    {"name": "April Sixth", "birthday": "2020.04.06"},
    {"name": "April Seventh", "birthday": "2020.04.07"},
    {"name": "April Eighth", "birthday": "2020.04.08"},
    {"name": "April Nineth", "birthday": "2024.07.07"},
    {"name": "April Tenth", "birthday": "2024.07.05"}
]

print(get_upcoming_birthdays(users))

