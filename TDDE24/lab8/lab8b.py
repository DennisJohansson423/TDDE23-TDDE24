# =========================================================================
# Type definition
# =========================================================================

# Define the type somehow...  The initial "" is simply here as a placeholder.

from typing import NamedTuple,List

from cal_abstraction import *
from cal_output import show_ts


TimeSpanSeq = NamedTuple("TimeSpanSeq",[("timespans",List[TimeSpan])])

# =========================================================================
#  Function implementations
# =========================================================================

# Implement these functions!  Also determine if you need *additional* functions.
  

def partition(ts_list:List[TimeSpan],low:int,high:int) -> tuple[int,List[TimeSpan]]:
    """ 
    To be used with quick_sort_ts to get the partition position.
    Returns the the postion of the  partition position and the sortedList.
    """
    
    # choose the rightmost element as pivot
    pivot = ts_list[high]

    # pointer for the later time
    i = low - 1
    
    for index in range(low, high): 
        if time_precedes_or_equals(ts_start(ts_list[index]),ts_start(pivot)):
            
            #if a time is earlier then the pivot
            #swap it with the later time pointed by i
            i = i + 1
            #swaping the time at i with the time at index
            (ts_list[i], ts_list[index]) = (ts_list[index], ts_list[i])

     # swap the pivot element with the later time specified by i
    (ts_list[i + 1], ts_list[high]) = (ts_list[high], ts_list[i + 1])
    #print(ts_list_copy,"return list")
    # return the position from where partition is done
    return (i + 1,ts_list)

def quick_sort_ts(ts_list:List[TimeSpan],low:int,high:int) -> List[TimeSpan]:
    """
    Implementing quick sort recursively to use the time sequence objeckt
    
    """
    ensure_type(ts_list,List[TimeSpan])
    ensure_type(low,int)
    ensure_type(high,int)

    # find pivot element such that
    # time earlier than pivot are on the left
    # time later than pivot are on the right
    if low < high:
        pi = partition(ts_list,low, high)
        quick_sort_ts(ts_list,low,pi[0] - 1)
        quick_sort_ts(ts_list,pi[0] + 1,high)

        return pi[1]

   


def new_time_span_seq(time_spans:List[TimeSpan] = None):
    """Creates and returns a new TimeSpanSeq with the given list."""
    if time_spans is None:
        time_spans_copy  = []
        return TimeSpanSeq(time_spans_copy)
    ensure_type(time_spans,List[TimeSpan])
    time_spans_copy = time_spans.copy()
    size = len(time_spans_copy) 
    if size  > 1:
        #Sorts the time in chronological order by using quick sort
        time_spans_copy = quick_sort_ts(time_spans_copy ,0,size -1 )
    return TimeSpanSeq(time_spans_copy)
        


def tss_is_empty(tss:TimeSpanSeq) -> bool:
    """Returns is the TimeSpanSeq is empty or not."""
    ensure_type(tss, TimeSpanSeq)
    return not tss.timespans


def time_span_seq_to_list(tss:TimeSpanSeq) -> List[TimeSpan]:
    """Returns the list that contains the TimeSpam objects."""
    ensure_type(tss, TimeSpanSeq)
    return tss.timespans

def tss_plus_span(tss:TimeSpanSeq, ts:TimeSpan) -> TimeSpanSeq:
    """
    Returns a copy of the given TimeSpanSeq, where the given TimeSpan
    has been added in its proper position.
    """
    ensure_type(tss, TimeSpanSeq)
    ensure_type(ts,TimeSpan)


    tss_list = time_span_seq_to_list(tss)

    def add_times_span(time:TimeSpan,time_span_seq_list:TimeSpanSeq):
        
        if not time_span_seq_list or time_precedes(
                ts_start(time), ts_start(time_span_seq_list[0])
        ):
            #Checks if the TimeSpan is befor the current first time in list
            return [time] + time_span_seq_list
        else:
            #Gose though the list recursively to find which positon to add the TimeSpan
             return [time_span_seq_list[0]] + add_times_span(time, time_span_seq_list[1:])
    return new_time_span_seq(add_times_span(ts,tss_list))


def tss_iter_spans(tss:TimeSpanSeq) -> TimeSpan:
    """To be used as `for time_span in cd_time_span_seq(tss)."""
    ensure_type(tss,TimeSpanSeq)
    for time_span in tss.timespans:
        yield time_span
   


def show_time_spans(tss:TimeSpanSeq) -> None:
    """Prints out the time span"""
    for ts in tss_iter_spans(tss):
        show_ts(ts)
        print()


# Keep only time spans that satisfy pred.
# You do not need to modify this function.
def tss_keep_spans(tss, pred):
    result = new_time_span_seq()
    for span in tss_iter_spans(tss):
        if pred(span):
            result = tss_plus_span(result, span)

    return result





time1 = new_time(new_hour(10), new_minute(15))
time2 = new_time(new_hour(13), new_minute(30))

time3 = new_time(new_hour(6),new_minute(3))
time4 = new_time(new_hour(8),new_minute(40))

time5 = new_time(new_hour(9),new_minute(54))
time6 = new_time(new_hour(11),new_minute(34))

span1 = new_time_span(time1, time2)
span2 = new_time_span(new_time_from_string("12:10"),new_time_from_string("15:45"))

span3 = new_time_span(time3,time4)


#9,6,12,10
span4 = new_time_span(time5, time6)

myTimeSpan = new_time_span_seq([span4,span3,span2,span1])


show_time_spans(myTimeSpan)
CLRnewMyTimeSpan = tss_plus_span(myTimeSpan,span2)



