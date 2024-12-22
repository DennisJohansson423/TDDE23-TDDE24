import math
import cv2
import numpy as np
from cvlib import rgblist_to_cvimg

"""Needed image for lab 5a."""
img = cv2.imread('plane.jpg')


#Lab 5A1
def cvimg_to_list(cv2_img):
    """Change the OpenCV picture to a list with BGR-tuples."""
    brg_list = []
    for row in cv2_img:
        for pixel in row:
            brg_list.append((pixel[0],pixel[1],pixel[-1]))
    return brg_list


def rgblist_to_cvimg(lst, height, width):
    """Return a width x height OpenCV image with specified pixels."""
    # A 3D array that will contain the image data
    img = np.zeros((height, width, 3), np.uint8)

    for x in range(0, width):
        for y in range(0, height):
            pixel = lst[y * width + x]
            img[y, x, 0] = pixel[0]
            img[y, x, 1] = pixel[1]
            img[y, x, 2] = pixel[2]
    return img

brg_list = cvimg_to_list(img)
converted_img = rgblist_to_cvimg(brg_list, img.shape[0], img.shape[1])

cv2.imshow("converted", converted_img)
cv2.waitKey(0)


#Lab 5A2
def negativ_gaussisk_blur(x, y):
    """Calculates the value for negative_gaussisk_blur."""
    if x == 0 and y == 0:
        return 1.5
    exponent = -(x**2 + y**2)/(2*4.5**2)
    base = -1/(2*math.pi*4.5**2)
    return base*math.e**exponent


def range_borders(N):
    """Determinates the range based on N."""
    if N % 2 == 0:
        return N//2, (N//2) - 1
    return N//2, N//2


def unsharp_mask(N):
    """The function returns a 2D list with the size NxN."""
    if N == 1:
        return [[1.5]]
    bottom , upper =range_borders(N)
    return [[negativ_gaussisk_blur(x, y) for y in range(-bottom,upper +1)] for x in range(-bottom,upper + 1)]


print(unsharp_mask(3))