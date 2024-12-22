# Write your code for lab 8d here.
from cal_abstraction import CalendarDay, Time
from cal_booking import is_booked_during
from cal_ui import book, create, get_calendar
from lab8a import get_ts_start_end
from lab8b import *
from settings import CHECK_AGAINST_FACIT

if CHECK_AGAINST_FACIT:
    try:
        from facit_la8_uppg import TimeSpanSeq
    except:
        print("*" * 100)
        print("*" * 100)
        print("Kan inte hitta facit; ändra CHECK_AGAINST_FACIT i test_driver.py till False")
        print("*" * 100)
        print("*" * 100)
        raise
else:
    from lab8b import *

def eval_app_overlap_span_start(app:Appointment,span:TimeSpan) -> bool:
    """Returns True if the Appointment overlapp with start time of span"""
    ensure_type(app,Appointment)
    ensure_type(span,TimeSpan)
    app_start = time_precedes_or_equals(ts_start(app_span(app)),ts_start(span))
    span_start = time_precedes_or_equals(ts_start(span),ts_end(app_span(app)))
    is_in_span = time_precedes(ts_end(app_span(app)),ts_end(span))
    return app_start and span_start and is_in_span



def eval_span_end(app:Appointment,span:TimeSpan) -> bool:
    """Returns True if the end time of span in overlapped by the appointment"""
    ensure_type(app,Appointment)
    ensure_type(span,TimeSpan)
    first_span = time_precedes_or_equals(ts_start(app_span(app)),ts_start(span))
    sec_span =  time_precedes_or_equals(ts_end(app_span(app)),ts_end(span))
    is_in_span = time_precedes(ts_start(span),ts_start(app_span(app)))
    return first_span and sec_span and is_in_span


def eval_app_overlap_span_end(app:Appointment,span:TimeSpan) -> bool:
    """Returns True if the end of the last span in overlapped.To be used when checking
        the last spans end
    """
    ensure_type(app,Appointment)
    ensure_type(span,TimeSpan)
    first_span = time_precedes_or_equals(ts_start(span),ts_end(app_span(app)))
    sec_span = time_precedes_or_equals(ts_end(span),ts_end(app_span(app)))
    is_in_span = time_precedes(ts_end(app_span(app)),ts_end(span))
    return first_span and sec_span and is_in_span

def eval_app_whole_span(app:Appointment,span:TimeSpan) -> bool:
    """Returns True if the appointment spans the whole span"""
    ensure_type(app,Appointment)
    ensure_type(span,TimeSpan)
    first_span = time_precedes_or_equals(ts_start(app_span(app)),ts_start(span))
    sec_span =  time_precedes_or_equals(ts_end(span),ts_end(app_span(app)))
    return first_span and sec_span

def eval_no_over_laping(app:Appointment,span:TimeSpan) -> bool:
    """Returns True if the appointment dose not overlap the span"""
    ensure_type(app,Appointment)
    ensure_type(span,TimeSpan)
    first_span = time_precedes_or_equals(ts_start(app_span(app)),ts_start(span))
    sec_span = time_precedes_or_equals(ts_end(span),ts_start(app_span(app)))

    return first_span or sec_span




def rest_app_check(appointment:Appointment,free_span_seq:TimeSpanSeq
    ) -> TimeSpanSeq:
    """Checks the appointnemt and decied how to update the free_span_seq"""

    ensure_type(appointment,Appointment)
    ensure_type(free_span_seq,TimeSpanSeq)

    list_time_span = time_span_seq_to_list(free_span_seq)

    time_seq_frist_span = list_time_span[0]
    time_seq_last_span = list_time_span[-1]

    if eval_app_whole_span(appointment,time_seq_frist_span):
        return new_time_span_seq()

    elif eval_app_overlap_span_start(appointment,time_seq_frist_span):
        #Check if a appointment is overlapping the first time
        new_span = new_time_span(ts_end(app_span(appointment)),
                                            ts_end(time_seq_frist_span))
        #Removes the old span that is now overwritten by new_span
        return tss_plus_span(new_time_span_seq(list_time_span[1:]),new_span) 

    elif eval_span_end(appointment,time_seq_last_span):
        #Check if the last span time end of the seq is overlapped
        new_span = new_time_span(ts_end(app_span(appointment)),
                                    ts_end(time_seq_last_span))
        return tss_plus_span(new_time_span_seq(list_time_span[:-1]),new_span)

    elif eval_app_overlap_span_end(appointment,time_seq_last_span): 
        #Check if the appointment begins befor the end and end after the end
        new_span = new_time_span(ts_start(time_seq_last_span),
                                    ts_start(app_span(appointment)))
        return tss_plus_span(new_time_span_seq(list_time_span[:-1]),new_span)

    elif eval_no_over_laping(appointment,time_seq_last_span):
        #IF no overlapping is found juste return the free_span_seq_uppdated
        return  free_span_seq
    #The case where the appoinetment is insie a free span    
    start_time = ts_start(time_seq_last_span)
    span_seq = new_time_span_seq(list_time_span[:-1])

    first_span = new_time_span(start_time,ts_start(app_span(appointment))) 
    sec_span = new_time_span(ts_end(app_span(appointment)),ts_end(time_seq_last_span))
    return tss_plus_span(tss_plus_span(span_seq,first_span),sec_span)


def appointment_check(cal_day: CalendarDay,free_span:TimeSpan) -> TimeSpanSeq:
    """Gose thought all appointmenta and updates the free_span_seq"""
    ensure_type(cal_day, CalendarDay)
    ensure_type(free_span,TimeSpan)

    free_span_seq = new_time_span_seq([free_span])
    for appointment in cd_iter_appointments(cal_day):
        free_span_seq = rest_app_check(appointment,free_span_seq )
        if tss_is_empty(free_span_seq):
            return free_span_seq
    return free_span_seq
  



def free_spans(cal_day: CalendarDay, start: Time, end: Time) -> TimeSpanSeq:
    """Calls the appointment_check function to get the  available and prints 
       them out
    """
    ensure_type(cal_day,CalendarDay)
    ensure_type(start,Time)
    ensure_type(end,Time)
    
    free_span_seq = appointment_check(cal_day,new_time_span(start,end))
    show_time_spans(free_span_seq)
    return free_span_seq
    

def show_free(cal_name:str,day:int,month:str,start_time:str,end_time:str) -> None:
    """Show the free time spans that are available."""
    ensure_type(cal_name,str)
    ensure_type(day,int)
    ensure_type(month,str)
    ensure_type(start_time,str)
    ensure_type(end_time,str)

    start = new_time_from_string(start_time)
    end = new_time_from_string(end_time)
    day = new_day(day)
    mon = new_month(month)
    cal_year = get_calendar(cal_name)
    cal_month = cy_get_month(mon, cal_year)
    cal_day = cm_get_day(cal_month, day)
    free_spans(cal_day,start,end)


