# This code violates abstraction layers, and should be reimplemented in lab 8A.
from cal_abstraction import *
from typing import Callable, Tuple


def get_time_number(ts: TimeSpan,time_diraction:Callable, 
    time_time : Callable, time_to_int :Callable ) -> int:
    """Takes a time span and returns the int represent of start or end and 
       minute or hour
    """
    ensure_type(ts,TimeSpan)
    
    ts = time_diraction(ts)         #End or start of ts
    ts_time = time_time(ts)         #Minute or hour
    ts_int = time_to_int(ts_time)   #Minute or hour to int

    return ts_int

def get_ts_start_end(ts:TimeSpan) -> Tuple[Time]:
    """Retuns both the start and end of a timespan"""
    ensure_type(ts,TimeSpan)
    ts_start_ = ts_start(ts)
    ts_end_ = ts_end(ts)
    return ts_start_, ts_end_

def ts_equals(ts1: TimeSpan, ts2: TimeSpan):
    """Return true iff the two given TimeSpans are equal."""
    ensure_type(ts1, TimeSpan)
    ensure_type(ts2, TimeSpan)
    ts1_start , ts1_end = get_ts_start_end(ts1)
    ts2_start , ts2_end = get_ts_start_end(ts2)
    
    return (time_equals(ts1_start, ts2_start) and
            time_equals(ts1_end, ts2_end))


def ts_overlap(ts1: TimeSpan, ts2: TimeSpan) -> bool:
    """Return true iff the two given TimeSpans overlap."""
    ensure_type(ts1, TimeSpan)
    ensure_type(ts2, TimeSpan)
    ts1_start , ts1_end = get_ts_start_end(ts1)
    
    ts2_start , ts2_end = get_ts_start_end(ts2)
    return (
            # TS1 isn't strictly after TS2
            time_precedes(ts1_start, ts2_start) and
            # TS2 isn't strictly after ts1
            time_precedes(ts1_end, ts2_end)
    )


def ts_overlapping_part(ts1: TimeSpan, ts2: TimeSpan) -> TimeSpan:
    """
    Return the overlapping part of two overlapping time spans,
    under the assumption that they really *are* overlapping.
    """
    ensure_type(ts1, TimeSpan)
    ensure_type(ts2, TimeSpan)
    ensure((ts1, ts2), lambda tup: ts_overlap(tup[0], tup[1]))

    # Tips: Det finns både snyggare och *enklare* sätt
    # att göra detta...
    
    ts1_start , ts1_end = get_ts_start_end(ts1)
    ts2_start , ts2_end = get_ts_start_end(ts2)

    start_time = time_latest(ts1_start,ts2_start)
    end_time = time_earliest(ts1_end,ts2_end)

    return new_time_span(start_time,end_time)   #overlapping_time_span


def ts_duration(ts: TimeSpan) -> "Duration":
    """Return the duration (length) of a TimeSpan."""
    ensure_type(ts, TimeSpan)


    ts_start_hour_int = hour_number(time_hour(ts_start(ts))) 

    ts_start_minute_int = minute_number(time_minute(ts_start(ts)))

    ts_end_hour_int = hour_number(time_hour(ts_end(ts))) 

    ts_end_minute_int = minute_number(time_minute(ts_end(ts)))

    mins = (
            ts_end_hour_int * 60 + ts_end_minute_int  -
            ts_start_hour_int * 60 - ts_start_minute_int
    )

    duration = new_duration(new_hour(mins // 60), new_minute(mins % 60))

    return duration


def duration_is_longer_or_equal(d1: Duration, d2: Duration):
    """
    Return true iff the first duration is longer than, or equally as long as,
    the second duration.
    """
    ensure_type(d1, Duration)
    ensure_type(d2, Duration)

    hours1 = hour_number(duration_hour(d1)) 
    hours2 =  hour_number(duration_hour(d2)) 
    mins1 = minute_number(duration_minute(d1)) 
    mins2 =  minute_number(duration_minute(d2)) 

    return (hours1, mins1) >= (hours2, mins2)


def duration_equals(d1: Duration, d2: Duration):
    """
    Return true if the first duration is equally as long as,
    the second duration.
    """
    ensure_type(d1, Duration)
    ensure_type(d2, Duration)

    hours1 = hour_number(duration_hour(d1)) 
    hours2 =  hour_number(duration_hour(d2)) 
    mins1 = minute_number(duration_minute(d1)) 
    mins2 =  minute_number(duration_minute(d2)) 

    return (hours1, mins1) == (hours2, mins2)




if __name__ == "__main__":
    time1 = new_time(new_hour(10), new_minute(15))
    time2 = new_time(new_hour(13), new_minute(30))
    span1 = new_time_span(time1, time2)
    span2 = new_time_span(new_time_from_string("12:10"),
                          new_time_from_string("15:45"))
    overlap = ts_overlapping_part(span1, span2)
    print(span1)
    print()
    print(span2)
    print()
    print(overlap)

    test_timespan_duration()
