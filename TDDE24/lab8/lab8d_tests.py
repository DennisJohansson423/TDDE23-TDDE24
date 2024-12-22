# Write your code for lab 8d here.

from test_driver import store_test_case, run_free_spans_tests


# Create additional test cases, and add to them to create_tests_for_free_span().

def create_tests_for_free_span() -> dict:
    """Create and return a number of test cases for the free_spans function"""
    test_cases = dict()

    store_test_case(
        test_cases,
        1,
        start_str="08:00",  # Search interval starts
        end_str="21:00",  # Search interval ends
        booking_data=["07:00-09:00", "13:00-18:00"],  # This day's appointments
        exp_result=["09:00-13:00", "18:00-21:00"],
    )  # Expected free time
     #-------- YOUR TEST CASES GO HERE -----------------------
    # For each case, add a brief description of what you want to test.
    store_test_case(
        test_cases,
        2, # Edgecase with two appointments
        start_str="08:00",
        end_str="21:00",
        booking_data=["08:00-09:00", "19:00-20:00"],
        exp_result=["09:00-19:00", "20:00-21:00"],
    )
    store_test_case(
        test_cases,
        3, # Test when it is multipel appointments in one day
        start_str="08:00",  # Search interval starts
        end_str="21:00",  # Search interval ends
        booking_data=["12:00-14:00", "15:00-16:00", "17.00-18:00"],  # This day's appointments
        exp_result=["08:00-12:00", "14:00-15:00", "16:00-17:00", "18:00-21:00"],
    )  # Expected free time

    store_test_case(
        test_cases,
        4, # Edgecase with no free time
        start_str="08:00",
        end_str="21:00",
        booking_data=["08:00-21:00"],
        exp_result=[],
    )

    store_test_case(
        test_cases,
        5, # Edgecase with no free time with two appointments
        start_str="08:00",
        end_str="21:00",
        booking_data=["08:00-17:00", "17:00-21:00"],
        exp_result=[],
    )

    store_test_case(
       test_cases,
        6, # Edgecase with appointments outside the span
        start_str="08:00",
        end_str="21:00",
        booking_data=["07:00-17:00", "17:00-22:00"],
        exp_result=[],
    )

    store_test_case(
        test_cases,
        7, # Edgecase with overlaping appointments
        start_str="08:00",
        end_str="21:00",
        booking_data=["08:00-11:00", "10:00-13:00", "14:00-16:00"],
        exp_result=["13:00-14.00", "16:00-21:00"],
    )

    store_test_case(
        test_cases,
        8, # Edgecase with no appointments booked
        start_str="08:00",
        end_str="21:00",
        booking_data=[],
        exp_result=["08:00-21:00"],
    )

    store_test_case(
        test_cases,
        9, # Edgecase with one appointment
        start_str="08:00",
        end_str="21:00",
        booking_data=["10:00-15:00"],
        exp_result=["08:00-10:00", "15:00-21:00"],
    )

    store_test_case(
        test_cases,
        10, # Edgecase where the whole free span is booked
        start_str="08:00",
        end_str="21:00",
        booking_data=["07:00-07:30"],
        exp_result=["08:00-21:00"],
    )

    store_test_case(
        test_cases,
        11, # Edgecase with start for app and frespan the same time
        start_str="08:00",
        end_str="21:00",
        booking_data=["08:00-12:15", "15:20-18:27"],
        exp_result=["12:15-15:20", "18:27-21:00"],
    )

    store_test_case(
        test_cases,
        12, # Edgecase where the whole free span is booked
        start_str="08:00",
        end_str="21:00",
        booking_data=["08:00-21:00"],
        exp_result=[],
    )
    store_test_case(
        test_cases,
        13, # Check that appoitments befor free span don't interfer
        start_str="08:00",
        end_str="21:00",
        booking_data=["01:00-02:00","08:00-21:00"],
        exp_result=[],
    )

    store_test_case(
        test_cases,
        14, # Check that if a time is booked that the other appoitments dont create 
        start_str="08:00", #free spans
        end_str="21:00",
        booking_data=["01:00-22:00","09:00-12:00"],
        exp_result=[],
    )


    store_test_case(
        test_cases,
        15, # Check when appointments start at the same time
        start_str="08:00", #free spans
        end_str="21:00",
        booking_data=["09:00-11:00","09:00-10:00"],
        exp_result=["08:00-09:00", "11:00-21:00"],
    )

   
    print("Test cases generated.")

    return test_cases


if __name__ == '__main__':
    # Actually run the tests, using the test driver functions
    tests = create_tests_for_free_span()
    run_free_spans_tests(tests)

def create_tests_for_free_span() -> dict:
    """Create and return a number of test cases for the free_spans function"""
    test_cases = dict()
    