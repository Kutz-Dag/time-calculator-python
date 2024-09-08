def add_time(start, duration, day = None):
    
    # start time
    start_hour, start_minute_am_or_pm = start.split(':')
    start_minute, am_or_pm = start_minute_am_or_pm.split(' ')
    start_hour = int(start_hour)
    start_minute = int(start_minute)

    # convert to digital clock
    if am_or_pm == "PM" and start_hour != 12:
        start_hour += 12
    elif am_or_pm == "AM" and start_hour == 12:
        start_hour = 0

    # duration
    duration_hour, duration_minute = duration.split(':')
    duration_hour = int(duration_hour)
    duration_minute = int(duration_minute)

    result_minute = start_minute + duration_minute
    result_hour = start_hour + duration_hour + (result_minute // 60)
    result_minute %= 60
    days_later = result_hour // 24
    result_hour %= 24

    # convert back to clock format
    if result_hour >= 12:
        am_or_pm = "PM"
        if result_hour > 12:
            result_hour -= 12
    else:
        am_or_pm = "AM"
        if result_hour == 0:
            result_hour = 12

    # if day argument is given 
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if day:
        day_of_week = days.index(day.capitalize())
        end_day = days[(day_of_week + days_later) % 7]
        result_day = f", {end_day}"
    else:
        result_day = ""

    # days later message to be returned
    if days_later == 0:
        days_later_return = ""
    elif days_later == 1:
        days_later_return = " (next day)"
    else:
        days_later_return = f" ({days_later} days later)"

    new_time = f"{result_hour}:{result_minute:02d} {am_or_pm}{result_day}{days_later_return}"

    return new_time

print(add_time('11:30 AM', '2:32', 'Monday'))
