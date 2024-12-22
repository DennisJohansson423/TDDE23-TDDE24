import cv2
import random
from cvlib import *
from lab5a import *

"""Needed images and lists for lab 5b."""
plane_img = cv2.imread('plane.jpg')
hsv_plane = cv2.cvtColor(plane_img, cv2.COLOR_BGR2HSV)
plane_list = cvimg_to_list(hsv_plane)
flowers_img = cv2.imread('flowers.jpg')
gradient_img = cv2.imread('gradient.jpg')
flowers_list = cvimg_to_list(flowers_img)
gradient_list = cvimg_to_list(gradient_img)


#Lab 5B1
def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):
    """
    Returns a function compareer that takes a pixel as input and
    returns the pixel if it is within the given constraints.
    """
    def pixel_in_range(pixel):
        if not isinstance(pixel, tuple):
            raise TypeError("Type is not an tuple")
        else:
            h, s, v = pixel
            return hlow <= h <= hhigh and slow <= s <= shigh and \
                     vlow <= v <= vhigh
    return pixel_in_range

is_sky = pixel_constraint(100, 150, 50, 200, 100, 255)
sky_pixels = list(map(lambda x: x * 255, map(is_sky, plane_list)))

cv2.imshow('sky', greyscale_list_to_cvimg(sky_pixels, hsv_plane.shape[0], hsv_plane.shape[1]))
cv2.waitKey(0)


#Lab 5B2
def generator_from_image(img_list):
    """
    Takes a image in list form and returns a function with a given index that
    returs the RGB value of the pixel at that index.
    """
    def generator(index):
        if index >= len(img_list):
            raise IndexError("Index out of bounds")
        return img_list[index]
    return generator

orig_img = cv2.imread('plane.jpg')
orig_list = cvimg_to_list(orig_img)
generator = generator_from_image(orig_list)
new_list = [generator(i) for i in range(len(orig_list))]

cv2.imshow('original', orig_img)
cv2.imshow('new', rgblist_to_cvimg(new_list, orig_img.shape[0], orig_img.shape[1]))
cv2.waitKey(0)


#Lab 5B3
def create_transform(condition, generator1, generator2):
    """This function calculates the new combined image."""
    def combine_pixels(px, i):
        return add_tuples(multiply_tuple \
                        (generator1(i), condition(px)), \
                        multiply_tuple \
                        (generator2(i), 1-condition(px)))
    return combine_pixels


def generator1(index):
    val = random.random() * 255 if random.random() > 0.99 else 0
    return (val, val, val)

generator2 = generator_from_image(cvimg_to_list(plane_img))
condition = pixel_constraint(100, 150, 50, 200, 100, 255)


def combine_images(img_list, condition, generator1, generator2):
    """Combine two genarated images."""
    try:
        combine_pixels = create_transform(condition, generator1, generator2)
        img_map = map(combine_pixels, img_list, range(len(img_list)))
        result = list(img_map)
    #Catch the incomming errors from the other functions and raise
    #a TypeError because the incomming type are then wrong
    except TypeError:
        raise TypeError
    except IndexError:
        raise TypeError
    return result

result = combine_images(plane_list, condition, generator1, generator2)
new_img = rgblist_to_cvimg(result, plane_img.shape[0], plane_img.shape[1])
cv2.imshow('Final image', new_img)
cv2.waitKey(0)


#Lab 5B4
def gradient_condition(px):
    return px[0] / 255

plane_list = cvimg_to_list(plane_img)
generator1 = generator_from_image(flowers_list)
generator2 = generator_from_image(plane_list)
result = combine_images(gradient_list, gradient_condition, generator1, generator2)

cv2.imshow('Combine image', rgblist_to_cvimg(result, gradient_img.shape[0], gradient_img.shape[1]))
cv2.waitKey(0)