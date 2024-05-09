from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    if days < 0:
        months -= 1
        days += 30

    if months < 0:
        years -= 1
        months += 12

    return years, months, days

# Input date of birth
dob = input("Enter your date of birth (dd-mm-yyyy): ")
dob_day, dob_month, dob_year = map(int, dob.split('-'))

# Create a datetime object for the date of birth
dob_datetime = datetime(dob_year, dob_month, dob_day)

# Calculate age
age_years, age_months, age_days = calculate_age(dob_datetime)

print(f"You are {age_years} years, {age_months} months, and {age_days} days old.")

