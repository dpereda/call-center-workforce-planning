import csv
from datetime import datetime, timedelta
import random
import math

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

# Special Events (campaigns, launches, etc.) with impact
SPECIAL_EVENTS = {
    '2/14/25': {'type': 'Marketing Campaign', 'impact': 1.25},  # Valentine's promo
    '3/15/25': {'type': 'Product Launch', 'impact': 1.40},  # Spring product
    '4/1/25': {'type': 'Billing Cycle', 'impact': 1.15},  # Monthly billing
    '5/1/25': {'type': 'Billing Cycle', 'impact': 1.15},
    '6/1/25': {'type': 'Billing Cycle', 'impact': 1.15},
    '7/1/25': {'type': 'Billing Cycle', 'impact': 1.15},
    '7/15/25': {'type': 'Summer Sale', 'impact': 1.30},  # Mid-summer promotion
    '8/1/25': {'type': 'Billing Cycle', 'impact': 1.15},
    '9/1/25': {'type': 'Billing Cycle', 'impact': 1.15},
    '9/15/25': {'type': 'Product Launch', 'impact': 1.35},  # Fall product
    '10/1/25': {'type': 'Billing Cycle', 'impact': 1.15},
    '11/1/25': {'type': 'Billing Cycle', 'impact': 1.15},
    '11/24/25': {'type': 'Black Friday', 'impact': 1.60},  # Huge spike
    '12/1/25': {'type': 'Billing Cycle', 'impact': 1.15},
    '12/15/25': {'type': 'Holiday Rush', 'impact': 1.35},  # Pre-Christmas
}

# Day-of-week multipliers (based on industry research)
# Monday typically busiest, Friday quieter, weekend much lower
DAY_MULTIPLIERS = {
    'Monday': 1.20,      # 20% above average
    'Tuesday': 1.10,     # 10% above average
    'Wednesday': 1.05,   # 5% above average
    'Thursday': 1.02,    # 2% above average
    'Friday': 0.98,      # 2% below average
    'Saturday': 0.85,    # 15% below average
    'Sunday': 0.75       # 25% below average
}

# Monthly seasonality indices (business has seasonal pattern)
# Jan/Feb (tax prep), Summer dip, Fall increase, Holiday spike
MONTHLY_MULTIPLIERS = {
    1: 1.15,   # January - New Year, tax questions
    2: 1.12,   # February - tax season
    3: 1.08,   # March - tax deadline approaching
    4: 1.05,   # April - post-tax normalization
    5: 1.00,   # May - baseline
    6: 0.95,   # June - summer slowdown
    7: 0.90,   # July - vacation season
    8: 0.92,   # August - still slow
    9: 1.05,   # September - back to business
    10: 1.10,  # October - Q4 ramp
    11: 1.15,  # November - holiday season
    12: 1.20   # December - year-end rush
}

# Base patterns from the example data (calls per 15-min interval)
# Represents a typical weekday pattern
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

# Weekend pattern - significantly lower volume
WEEKEND_PATTERN = {k: int(v * 0.4) for k, v in WEEKDAY_PATTERN.items()}

# Holiday pattern - minimal volume
HOLIDAY_PATTERN = {k: int(v * 0.15) for k, v in WEEKDAY_PATTERN.items()}

def get_growth_multiplier(day_number):
    """
    Calculate growth multiplier for given day (7% annual growth trend).
    This creates a gradual upward trend throughout the year.
    """
    return 1 + (0.07 * day_number / 365)

def get_monthly_multiplier(date):
    """Get seasonal multiplier based on month"""
    return MONTHLY_MULTIPLIERS.get(date.month, 1.0)

def get_day_multiplier(day_name):
    """Get day-of-week multiplier"""
    return DAY_MULTIPLIERS.get(day_name, 1.0)

def get_special_event_impact(date_str):
    """Check if date has special event and return impact multiplier"""
    event = SPECIAL_EVENTS.get(date_str)
    if event:
        return event['impact'], event['type']
    return 1.0, None

def calculate_calls(base_calls, current_date, day_number, day_name, variation=0.12):
    """
    Calculate calls with multiple layers of realism:
    - Base pattern (intraday)
    - Growth trend (annual)
    - Monthly seasonality
    - Day-of-week pattern
    - Special events
    - Random variation
    """
    date_str = current_date.strftime('%-m/%-d/%y')

    # Layer 1: Growth trend
    growth = get_growth_multiplier(day_number)

    # Layer 2: Monthly seasonality
    monthly = get_monthly_multiplier(current_date)

    # Layer 3: Day-of-week pattern
    day_mult = get_day_multiplier(day_name)

    # Layer 4: Special events
    event_impact, event_type = get_special_event_impact(date_str)

    # Layer 5: Random variation (reduced from 0.15 to 0.12 for more realistic data)
    random_factor = random.uniform(1 - variation, 1 + variation)

    # Combine all factors
    final_calls = base_calls * growth * monthly * day_mult * event_impact * random_factor

    return max(0, int(round(final_calls))), event_type

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
    """Generate a full year of call center data with realistic patterns"""
    start_date = datetime(2025, 1, 1)
    end_date = datetime(2025, 12, 31)

    output_file = 'call_center_annual_data.csv'

    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = [
            'Day', 'Date', 'Time_Interval', 'Calls_Offered', 'Calls_Answered',
            'Calls_Abandoned', 'Abandonment_Rate_%', 'Average_Handle_Time_Seconds',
            'Average_Speed_of_Answer_Seconds', 'Day_Type', 'Holiday_Name', 'Special_Event'
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
                calls_offered, event_type = calculate_calls(
                    base_calls, current_date, day_number, day_name
                )
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
                    'Holiday_Name': holiday_name,
                    'Special_Event': event_type if event_type else ''
                })

            current_date += timedelta(days=1)

    print(f"✓ Generated {output_file}")
    print(f"✓ Total days: {day_number}")
    print(f"✓ Total records: {day_number * 36} (36 intervals per day)")
    print(f"✓ Includes:")
    print(f"  - 7% annual growth trend")
    print(f"  - Monthly seasonality (tax season, summer dip, holiday rush)")
    print(f"  - Day-of-week patterns (Monday highest, weekend lowest)")
    print(f"  - {len(US_HOLIDAYS)} US federal holidays")
    print(f"  - {len(SPECIAL_EVENTS)} special events (campaigns, product launches, billing cycles)")
    print(f"✓ Perfect for testing forecasting methods!")

if __name__ == '__main__':
    random.seed(42)  # For reproducible results
    generate_annual_data()
