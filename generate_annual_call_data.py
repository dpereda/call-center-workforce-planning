import csv
from datetime import datetime, timedelta
import random

# US Federal Holidays for 2025
US_HOLIDAYS = {
    '1/1/25': "New Year's Day",
    '1/20/25': "MLK Jr. Day",
    '2/17/25': "Presidents' Day",
    '5/26/25': "Memorial Day",
    '7/4/25': "Independence Day",
    '9/1/25': "Labor Day",
    '10/13/25': "Columbus Day",
    '11/11/25': "Veterans Day",
    '11/27/25': "Thanksgiving",
    '11/28/25': "Day after Thanksgiving",
    '12/24/25': "Christmas Eve",
    '12/25/25': "Christmas Day",
    '12/31/25': "New Year's Eve"
}

# Base patterns from the example data (calls per 15-min interval)
# Weekday pattern (Monday-Friday)
WEEKDAY_PATTERN = {
    '08:00-08:15': 16, '08:15-08:30': 12, '08:30-08:45': 9, '08:45-09:00': 8,
    '09:00-09:15': 24, '09:15-09:30': 17, '09:30-09:45': 13, '09:45-10:00': 11,
    '10:00-10:15': 30, '10:15-10:30': 21, '10:30-10:45': 17, '10:45-11:00': 14,
    '11:00-11:15': 28, '11:15-11:30': 19, '11:30-11:45': 16, '11:45-12:00': 13,
    '12:00-12:15': 19, '12:15-12:30': 13, '12:30-12:45': 10, '12:45-13:00': 9,
    '13:00-13:15': 23, '13:15-13:30': 16, '13:30-13:45': 13, '13:45-14:00': 10,
    '14:00-14:15': 26, '14:15-14:30': 18, '14:30-14:45': 15, '14:45-15:00': 12,
    '15:00-15:15': 20, '15:15-15:30': 14, '15:30-15:45': 11, '15:45-16:00': 9,
    '16:00-16:15': 17, '16:15-16:30': 12, '16:30-16:45': 9, '16:45-17:00': 7
}

# Weekend pattern (Saturday-Sunday) - about 40% of weekday volume
WEEKEND_PATTERN = {k: int(v * 0.4) for k, v in WEEKDAY_PATTERN.items()}

# Holiday pattern - about 15% of weekday volume
HOLIDAY_PATTERN = {k: int(v * 0.15) for k, v in WEEKDAY_PATTERN.items()}

def get_growth_multiplier(day_number):
    """Calculate growth multiplier for given day (7% annual growth)"""
    return 1 + (0.07 * day_number / 365)

def calculate_calls(base_calls, day_number, variation=0.15):
    """Calculate calls with growth trend and random variation"""
    growth_multiplier = get_growth_multiplier(day_number)
    varied_calls = base_calls * growth_multiplier * random.uniform(1 - variation, 1 + variation)
    return max(0, int(round(varied_calls)))

def calculate_metrics(calls_offered):
    """Calculate other call metrics based on calls offered"""
    if calls_offered == 0:
        return 0, 0, 0, 264, 20

    # Abandonment increases with higher call volumes
    if calls_offered < 10:
        abandonment_rate = random.uniform(0, 0.03)
    elif calls_offered < 20:
        abandonment_rate = random.uniform(0.02, 0.06)
    elif calls_offered < 30:
        abandonment_rate = random.uniform(0.04, 0.08)
    else:
        abandonment_rate = random.uniform(0.05, 0.10)

    calls_abandoned = int(round(calls_offered * abandonment_rate))
    calls_answered = calls_offered - calls_abandoned

    # Average Handle Time: 258-282 seconds
    aht = random.randint(258, 282)

    # Average Speed of Answer increases with volume
    if calls_offered < 10:
        asa = random.randint(18, 30)
    elif calls_offered < 20:
        asa = random.randint(25, 40)
    elif calls_offered < 30:
        asa = random.randint(35, 50)
    else:
        asa = random.randint(45, 60)

    return calls_answered, calls_abandoned, abandonment_rate, aht, asa

def generate_annual_data():
    """Generate a full year of call center data"""
    start_date = datetime(2025, 1, 1)
    end_date = datetime(2025, 12, 31)

    output_file = 'call_center_annual_data.csv'

    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = [
            'Day', 'Date', 'Time_Interval', 'Calls_Offered', 'Calls_Answered',
            'Calls_Abandoned', 'Abandonment_Rate_%', 'Average_Handle_Time_Seconds',
            'Average_Speed_of_Answer_Seconds', 'Day_Type', 'Holiday_Name'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        current_date = start_date
        day_number = 0

        while current_date <= end_date:
            day_number += 1
            day_name = current_date.strftime('%A')
            date_str = current_date.strftime('%-m/%-d/%y')

            # Determine day type and pattern
            is_weekend = day_name in ['Saturday', 'Sunday']
            is_holiday = date_str in US_HOLIDAYS
            holiday_name = US_HOLIDAYS.get(date_str, '')

            if is_holiday:
                pattern = HOLIDAY_PATTERN
                day_type = f'HOLIDAY: {holiday_name}'
            elif is_weekend:
                pattern = WEEKEND_PATTERN
                day_type = 'WEEKEND'
            else:
                pattern = WEEKDAY_PATTERN
                day_type = 'Weekday'

            # Generate data for each 15-minute interval
            for time_interval, base_calls in pattern.items():
                calls_offered = calculate_calls(base_calls, day_number)
                calls_answered, calls_abandoned, abandonment_rate, aht, asa = calculate_metrics(calls_offered)

                # Format abandonment rate as percentage
                abandonment_pct = f"{abandonment_rate * 100:.2f}%"

                writer.writerow({
                    'Day': day_name,
                    'Date': date_str,
                    'Time_Interval': time_interval,
                    'Calls_Offered': calls_offered,
                    'Calls_Answered': calls_answered,
                    'Calls_Abandoned': calls_abandoned,
                    'Abandonment_Rate_%': abandonment_pct,
                    'Average_Handle_Time_Seconds': aht,
                    'Average_Speed_of_Answer_Seconds': asa,
                    'Day_Type': day_type,
                    'Holiday_Name': holiday_name
                })

            current_date += timedelta(days=1)

    print(f"✓ Generated {output_file}")
    print(f"✓ Total days: {day_number}")
    print(f"✓ Total records: {day_number * 36}")
    print(f"✓ Weekends and holidays are marked in the 'Day_Type' column")
    print(f"✓ 7% annual growth trend applied")

if __name__ == '__main__':
    random.seed(42)  # For reproducible results
    generate_annual_data()
