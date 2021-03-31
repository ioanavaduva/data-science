def add_time(start, duration, day=''):

    start_split = start.split(' ')

    hrs_min_start = start_split[0].split(':')

    hrs_min_duration = duration.split(':')

    hrs = int(hrs_min_start[0]) + int(hrs_min_duration[0])
    mins = int(hrs_min_start[1]) + int(hrs_min_duration[1])

    if mins >= 60:
        hrs = hrs+1
        mins = mins % 60
    else:
        pass

    if start_split[1] == 'AM' and hrs >= 12 and hrs < 24: 
        am_pm = 'PM'
    elif start_split[1] == 'PM' and hrs >= 12:
        am_pm = 'AM'
    # elif start_split[1] == 'AM' and hrs > 24:
    #     am_pm = 'AM'
    # elif start_split[1] == 'PM' and hrs > 24:
    #     am_pm = 'PM'
    else:
        am_pm = start_split[1]

    if hrs > 12:
        hrs = hrs%12
        if hrs == 0:
            hrs = 12

    extra_days = int(hrs_min_duration[0]) // 24
    if start_split[1] == 'AM' and int(hrs_min_duration[0]) > 12 and int(hrs_min_duration[0]) < 24 and am_pm == 'AM':
        extra_days = extra_days + 1
    elif start_split[1] == 'PM' and am_pm == 'AM':
        extra_days = extra_days + 1
    else:
        pass

    if extra_days == 1:
        days_later = ' (next day)'
    elif extra_days > 1:
        days_later = ' (' + str(extra_days) + ' days later)'
    else:
        days_later = ''
    
    days_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    day = day.capitalize()
    
    if day == '':
        days_output = ''
        pass
    else:
        days_index_output = days_week.index(day) + extra_days
        days_output = ', ' + days_week[days_index_output % len(days_week)]

    new_time = str(hrs) + ':' + str(mins).zfill(2) + ' ' + am_pm + days_output + days_later

    return new_time

print(add_time('3:00 PM', '3:10'))
print(add_time('11:30 AM', '2:32', 'Monday'))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30")) 
print(add_time("11:43 PM", "24:20", 'tueSday')) 
print(add_time("6:30 PM", "205:12")) 
print(add_time("2:59 AM", "24:00"))
