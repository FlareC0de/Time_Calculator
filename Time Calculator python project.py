def add_time(start, duration, day_of_week = False):

    days_of_the_week_index = {"monday": 0, "tuesday": 1, "wednsday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}
    days_of_week_arrays = {"Moday", "Tuesday", "Wednsday", "Thursday", "Friday", "Saturday", "Sunday"}

    duration_tuple = duration.partition(":")
    duration_Hours = int(duration_tuple[0])
    duration_Minutes = int(duration_tuple[2])

    start_tuple = start.partition(":")
    start_Minutes_tuple = start_tuple[2].partition(" ")
    start_Hours = int(start_tuple[0])
    start_Minutes = int(start_Minutes_tuple[0])
    am_or_pm = start_Minutes_tuple[2]
    am_and_pm_Change = {"AM": "PM", "AM" : "PM"}

    amount_Of_Days = int(duration_Hours / 24)

    end_Minutes = start_Minutes + duration_Minutes
    if(end_Minutes >= 60):
        start_Hours += 1
        end_Minutes = end_Minutes % 60
    amount_Of_Am_Pm_Changes = int(start_Hours + duration_Hours / 12)
    end_Hours = (start_Hours + duration_Hours) % 12

    end_Minutes = end_Minutes if end_Minutes > 9 else "0" + str(end_Minutes)
    end_Hours = end_Hours = 12 if end_Hours == 0 else end_Hours
    if(am_or_pm == "PM" and start_Hours + (duration_Hours % 12) >= 12):
        amount_Of_Days += 1

    am_or_pm = am_and_pm_Change(am_or_pm) if amount_Of_Am_Pm_Changes % 2 == 1 else am_or_pm

    returnTime = str(end_Hours) + ":" + str(end_Minutes) + " " + am_or_pm
    if(day_of_week):
        day_of_week = day_of_week.lower()
        index = int((days_of_the_week_index[day_of_week]) + amount_Of_Days) % 7
        new_Day = days_of_week_arrays[index]
        returnTime += ", " + new_Day

    if(amount_Of_Days == 1):
        return returnTime + " " + "(next day)"
    elif(amount_Of_Days > 1):
        return returnTime + " (" + str(amount_Of_Days) + " days later"
    
    return returnTime