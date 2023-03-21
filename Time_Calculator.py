def add_time (Start_Time, Add_Time, Day =""):
    Final_Time = 0

    Nex_Day = " "
    The_days = ["Monday", "Tuesday", "Wednesday","Thursday","Friday","Saturday", "Sunday"]



    Start_Time = Start_Time.split()             #separating with space
    Clock_Minutes = Start_Time[0]               # extracting time
    Clock_Minutes = Clock_Minutes.split(':')    #separating clock and minutes
    Clock = Clock_Minutes[0]                     #clock
    Minutes = Clock_Minutes[1]                   #minutes
    Start_Time_AM_PM = Start_Time[1]             #AM or PM
    #print(Start_Time_AM_PM)

    Add_Time = Add_Time.split(':')               #separatin clock and minutes
    Add_clock = int(Add_Time[0])%12              #getting clock
    Flag_AM_PM = int(Add_Time[0]) / 12
    Days = round(int(Add_Time[0])/24)
    Add_Time_Minutes = Add_Time[1]               #getting minutes



    updated_time_clock = int(Clock)+Add_clock                  # sum of the clock
    updated_time_minutes = int(Minutes)+int(Add_Time_Minutes)       # sum of minutes
    Start_Time_AM_PM_Updated =  Start_Time_AM_PM                    # AM or PM

    if updated_time_clock >=12 and Days > 0 and int(updated_time_minutes) > 0  :
        Days = Days + 1

    if updated_time_clock >= 12 and updated_time_minutes < 60 :
        updated_time_clock = updated_time_clock - 12

        if (Start_Time_AM_PM == 'PM') :
            Start_Time_AM_PM_Updated = "AM"

        else:
            Start_Time_AM_PM_Updated = "PM"



    elif updated_time_clock >= 12 and updated_time_minutes >= 60 :

        updated_time_clock = updated_time_clock +1 - 12
        updated_time_minutes = 60 - updated_time_minutes
        if updated_time_minutes <0 :
            updated_time_minutes = updated_time_minutes*(-1)

        elif updated_time_minutes == 0:
            updated_time_minutes = '00'

        if (Start_Time_AM_PM == 'PM'):
            Start_Time_AM_PM_Updated = "AM"
        else:
            Start_Time_AM_PM_Updated = "PM"


    elif updated_time_clock < 12 and updated_time_minutes >= 60 :
        updated_time_clock = updated_time_clock +1
        updated_time_minutes = 60 - updated_time_minutes

        if updated_time_minutes == 0:
            zero_minutes ='00'


        if updated_time_minutes < 0:
            updated_time_minutes = updated_time_minutes * (-1)

        if updated_time_clock >=12 and Start_Time_AM_PM == 'PM':
            Start_Time_AM_PM_Updated = "AM"
        else:
            Start_Time_AM_PM_Updated = "PM"

    else:
        updated_time_clock = updated_time_clock
        updated_time_minutes = updated_time_minutes
    later = " "
    if Days >0 :
        later = "Later"

    if Start_Time_AM_PM_Updated == "AM" and updated_time_clock >=12  :

        if Day == "Monday":
            Nex_Day = The_days[1]
        elif Day == "Tuesday":
            Nex_Day = The_days[2]
        elif Day == "Wednesday":
            Nex_Day = The_days[3]
        elif Day == "Thursday":
            Nex_Day = The_days[4]
        elif Day == "Friday":
            Nex_Day = The_days[5]
        elif Day == "Saturday":
            Nex_Day = The_days[6]
        elif Day == "Sunday":
            Nex_Day = The_days[0]

    if updated_time_minutes == 0:
            zero_minutes ='00'
            if updated_time_clock >= 12 and Days > 0 and int(updated_time_minutes) > 0:
                Days = Days + 1
            print(updated_time_clock,':',zero_minutes,' ',Start_Time_AM_PM_Updated, ' Days :', Days, later, Nex_Day)
    else:
        if updated_time_clock >= 12 and Days > 0 and int(updated_time_minutes) > 0:
            Days = Days + 1

        print(updated_time_clock, ':', updated_time_minutes, ' ', Start_Time_AM_PM_Updated, ' Days :', Days, later, Nex_Day )


    return Final_Time
