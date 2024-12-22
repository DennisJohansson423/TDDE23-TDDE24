from cal_abstraction import *
from cal_booking import *
from cal_ui import *


def update_calender(name:str,day_int:int,start_time: str,calender:CalendarYear,month_objeckt:Month) -> CalendarYear:
    """
    Returns a new CalendarYear where an appointment, specified by the parameters,
    has been removed in the appropriate CalendarDay. 

    The function is intend to be used with the remove function
    """
    ensure_type(name,str)
    ensure_type(day_int,int)
    ensure_type(start_time,str)
    ensure_type(calender,CalendarYear)
    ensure_type(month_objeckt,Month)
    new_calendar(name)   #The calender is reset
    updated_calender = get_calendar(name)
    for cal_month in cy_iter_months(calender):
        #If the month number dose not match the appointment month, the we can 
        #add it directly to updated_calender
        if month_number(cm_month(cal_month)) != month_number(month_objeckt):
            updated_calender = cy_plus_cm(updated_calender,cal_month)
        else:
            updated_month = update_month(day_int,start_time,cal_month )
            #If the month is empty we dont wont to add it to the calenderYear
            if not cm_is_empty(updated_month): 
                updated_calender = cy_plus_cm(updated_calender,updated_month)
    return updated_calender


def update_month(day_int:int,start_time:str,month_objeckt:CalendarMonth) -> CalendarMonth:
    """
    Returns a new CalendarMonth where an appointment, specified by the parameters,
    has been removed in the appropriate CalendarDay. If the CalendarMonth is empty
    None is returnd.

    The function is intend to be used with the update_calender function
    """
    ensure_type(day_int,int)
    ensure_type(start_time,str)
    ensure_type(month_objeckt,CalendarMonth)

    updated_month = new_month(month_name(cm_month(month_objeckt)))
    updated_cm = new_calendar_month(updated_month )
    for cal_day in cm_iter_days(month_objeckt):
        #If the day number dose not match the appointment month, the we can 
        #add it directly to updated_cm
        if day_number(cd_day(cal_day)) != day_int:
            updated_cm = cm_plus_cd(updated_cm ,cal_day)
        else:
            updated_day = update_day(start_time,cal_day)
            #If the day is empty we dont wont to add it to the calenderMonth
            if not cd_is_empty(updated_day):
                updated_cm = cm_plus_cd(updated_cm,updated_day)
    return updated_cm


def update_day(start_time:str,calender_day: CalendarDay) ->  CalendarDay:
    """
    Returns a new  CalendarDay where an appointment, specified by the parameters,
    has been removed in the appropriate CalendarDay. If the CalendarDay is empty
    None is returnd.

    The function is intend to be used with the update_month function
    """
    ensure_type(start_time,str)
    ensure_type(calender_day,CalendarDay)
    updated_day = new_day(day_number(cd_day(calender_day)))
    updated_cd = new_calendar_day(updated_day)
    start_time_objeckt = new_time_from_string(start_time)
    for appointment in cd_iter_appointments(calender_day):
        appointment_span = app_span(appointment)
        appointment_start_time = ts_start(appointment_span)
        if not time_equals(appointment_start_time, start_time_objeckt):
            updated_day = cd_plus_appointment(updated_cd,appointment)
    
    return updated_day


def remove(name:str, day_int:int, month_name:str, start_time:str)-> None:
    """
    Return a new CalendarYear where an appointment, specified by the parameters,
    has been removed in the appropriate CalendarDay.
    """
    calender = get_calendar(name)
    month_objeckt = new_month(month_name)
    time = new_time_from_string(start_time)
    day = new_day(day_int)

    calender_month = cy_get_month(month_objeckt,calender)
    calender_day = cm_get_day(calender_month, day)
    if not is_booked_from(calender_day, time):
        print("Theres nothing there to remove")
    else:
        updated_calender = update_calender(name, day_int, start_time, calender, month_objeckt)
        insert_calendar(name, updated_calender)
        print("The appointment has been remvode.")


create("Jayne")
book("Jayne", 20, "sep", "12:00", "14:00", "Rob train")
book("Jayne", 20, "sep", "15:00", "16:00", "Escape with loot")
show("Jayne", 20, "sep")
remove("Jayne", 20, "sep", "15:00")
book("Jayne", 20, "sep", "15:00", "16:00", "Return loot")
show("Jayne", 20, "sep")