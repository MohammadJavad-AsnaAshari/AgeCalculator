from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()
    age_years = today.year - birth_date.year
    age_months = today.month - birth_date.month
    age_days = today.day - birth_date.day

    # Adjust for negative months or days
    if age_days < 0:
        # Borrow from months
        age_months -= 1
        # Calculate the number of days in the birth month
        days_in_birth_month = (
                    birth_date.replace(month=birth_date.month % 12 + 1, day=1) - birth_date.replace(day=1)).days
        age_days += days_in_birth_month

    if age_months < 0:
        # Borrow from years
        age_years -= 1
        age_months += 12

    return age_years, age_months, age_days

def main():
    birth_day = int(input("Enter the day of birth (1-31): "))
    birth_month = int(input("Enter the month of birth (1-12): "))
    birth_year = int(input("Enter the year of birth: "))

    birth_date = datetime(birth_year, birth_month, birth_day)
    age_years, age_months, age_days = calculate_age(birth_date)

    # Determine the pluralization for each part
    year_label = 'year' if age_years == 1 else 'years'
    month_label = 'month' if age_months == 1 else 'months'
    day_label = 'day' if age_days == 1 else 'days'

    # Format the output
    result = f"Your age is {age_years} {year_label}"
    if age_months > 0:
        month_label = 'month' if age_months == 1 else 'months'
        result += f", {age_months} {month_label}"
    if age_days > 0:
        day_label = 'day' if age_days == 1 else 'days'
        result += f", and {age_days} {day_label}"

    today = datetime.today()
    if today.month == birth_month and today.day == birth_day:
        result += "\nHappy birthday!"

    print(result)

if __name__ == "__main__":
    main()
