from lab5a import *
from lab5b import *

def run_tests():
    """Call this function to run the tests."""
    try:
        test_pixel_constraint()
        print("This code passed pixel_constraint tests")
    except AssertionError:
        print("This code failed pixel_constraint tests")
        raise
    try:
        test_generator_from_image()
        print("This code passed all generator_from_image tests")
    except AssertionError:
        print("This code failed generator_from_image tests")
        raise
    try:
        test_combine_images()
        print("This code passed all combine_image tests")
    except AssertionError:
        print("This code failed combine_image tests")
        raise
    print("This code passed all tests")


def test_pixel_constraint():
    """Test pixel constraint function."""
    false_test_cases = (((100, 150, 50, 200, 100, 255), (ValueError)) \
                        ,((ValueError, 150, 50, 200, 100, 255), (120, 100, 150)))
    
    test_cases = (((100, 150, 50, 200, 100, 255), (120, 100, 150)) \
                    ,((160, 90, 220, 30, 250, 100), (100, 180, 150)) \
                    ,((0, 255, 0, 300, 0, 260), (150, 200, 180)))

    expected_results = ((1), (0), (1))
    
    for elem in false_test_cases:
        try:
            pixel_constraint(elem[0][0], elem[0][1], elem[0][2], elem[0][3], elem[0][4], elem[0][5])
        except TypeError:
            assert True

    for elem, expected in zip(test_cases, expected_results):
        pc = pixel_constraint(elem[0][0], elem[0][1], elem[0][2], elem[0][3], elem[0][4], elem[0][5])
        assert pc(elem[1]) == expected, "Expected {} got {}".format(expected, pc(elem[1]))


def test_generator_from_image():
    """Test generator from image function."""
    false_test_cases = ((((ValueError), (160, 155, 255), (20, 80, 175)), 0) \
                        ,(((200, 100, 150), (160, 155, 255), (20, 80, 175)), ValueError))

    test_cases = ((((100, 100, 100), (50, 120, 255), (260, 255, 300)), 2) \
                    ,(((260, 200, 80), (180, 50, 255), (00, 000, 255)), 0))

    expected_result = ((260, 255, 300), (260, 200, 80))

    for elem in false_test_cases:
        try:
            generator_from_image([elem[0][0], elem[0][1], elem[0][2]])
        except TypeError:
            assert True

    for elem, expected in zip(test_cases, expected_result):
        gfi = generator_from_image([elem[0][0], elem[0][1], elem[0][2]])
        assert gfi(elem[1]) == expected, "Expected {} got {}".format(
            expected, gfi(elem[1]))


def test_combine_images():
    """Test combine images function."""
    img_list = ([(100, 100, 100), (50, 120, 255), (260, 255, 300)] \
                ,[(260, 200, 80), (180, 50, 255), (00, 000, 255)] \
                ,[(100, 100, 100), (30, 50, 255), (175, 200, 80)] \
                ,[(ValueError), (30, 50, 255), (175, 200, 80)])
    
    conditions = ((pixel_constraint(100, 150, 50, 200, 100, 255)) \
                ,(pixel_constraint(160, 90, 220, 30, 250, 100)) \
                ,(pixel_constraint(150, 80, 210, 30, 250, 100)) \
                ,(pixel_constraint(100, 160, 60, 200, 90, 245)))

    generator1 = ((generator_from_image([(255, 0, 0), (255, 0, 0), (255, 0, 0)])) \
                ,(generator_from_image([(0, 255, 0), (0, 255, 0), (0, 255 ,0)])) \
                ,(generator_from_image([(255, 0, 0), (255, 0, 0), (255, 0, 0)])) \
                ,(generator_from_image([(0, 255, 0), (0, 255, 0), (0, 255, 0)])))
    
    generator2 = ((generator_from_image([(0, 0, 255), (0, 20, 0), (0, 10, 0)])) \
                ,(generator_from_image([(0, 0, 255), (0, 20, 0), (0, 10, 0)])) \
                ,(generator_from_image([(0, 255, 0), (0, 0, 0), (0, 0 ,0)])) \
                ,(generator_from_image([(0, 0, 0), (0, 0, 0), (0, 0, 0)])))

    test_cases = (((img_list[0]), (conditions[0]), (generator1[0]), (generator2[0])) \
                ,((img_list[1]), (conditions[1]), (generator1[1]), (generator2[1])) \
                ,((img_list[2]), (conditions[2]), (generator1[2]), (generator2[2])))

    expected_results = ((255, 0, 0), (0, 0, 255), (0, 255, 0))

    try:
        combine_images((img_list[3]), (conditions[3]), (generator1[3]), (generator2[3]))
    except TypeError:
        assert True
    for elem, expected in zip(test_cases, expected_results):
        ci = combine_images(elem[0], elem[1], elem[2], elem[3])
        assert ci[0] == expected, "Expected {} got {}".format(
            expected, ci[0])


run_tests()