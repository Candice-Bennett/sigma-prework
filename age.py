import datetime
def age_calculator(input_date: str) -> int:
    current_date = datetime.date.today()
    day,month,year = map(int, input_date.split("-"))
    if current_date.month >= month & current_date.day >= day:
        return current_date.year - year 
    else: 
        return current_date.year - year - 1

print(age_calculator("14-05-2000"))

