# import packages: numpy, math (you might need pi for gaussian functions)
import numpy as np
from math import *
import matplotlib.pyplot as plt
from scipy.signal import convolve2d as conv2
from scipy.ndimage import convolve1d as conv1



"""
Gaussian function taking as argument the standard deviation sigma
The filter should be defined for all integer values x in the range [-3sigma,3sigma]
The function should return the Gaussian values Gx computed at the indexes x
"""


def gauss(sigma):
    x = np.array(list(range(-3 * int(sigma), (3 * int(sigma)) + 1)))
    g_x = np.exp(-np.power(x, 2.) / (2 * np.power(sigma, 2.))) / (sigma * np.power(2 * np.pi, 0.5))
    return g_x, x


"""
Implement a 2D Gaussian filter, leveraging the previous gauss.
Implement the filter from scratch or leverage the convolve2D method (scipy.signal)
Leverage the separability of Gaussian filtering
Input: image, sigma (standard deviation)
Output: smoothed image
"""


def gaussianfilter(img, sigma):
    [Gx, x] = gauss(sigma)
    Gy = Gx.T
    intermediate = np.zeros(img.shape)
    smooth_img = np.zeros(img.shape)
    h = img.shape[0]
    w = img.shape[1]
    for i in range(h):
        intermediate[i] = conv1(img[i], Gx, mode="reflect")
    for i in range(w):
        smooth_img[:, i] = conv1(intermediate[:, i], Gy, mode="reflect")
    return smooth_img



"""
Gaussian derivative function taking as argument the standard deviation sigma
The filter should be defined for all integer values x in the range [-3sigma,3sigma]
The function should return the Gaussian derivative values Dx computed at the indexes x
"""


def gaussdx(sigma):
    x = np.array(list(range(-3 * int(sigma), (3 * int(sigma)) + 1)))
    d_x = x * np.exp(-np.power(x, 2.) / (2 * np.power(sigma, 2.))) / (np.power(sigma, 3) * np.power(2 * np.pi, 0.5))
    return d_x, x


def gaussderiv(img, sigma):
    [Dx, x] = gaussdx(sigma)
    Dy = Dx.T
    imgDx = np.zeros(img.shape)
    imgDy = np.zeros(img.shape)
    smooth_img = np.zeros(img.shape)
    h = img.shape[0]
    w = img.shape[1]
    smooth_img = gaussianfilter(img, sigma)
    for i in range(h):
        imgDx[i] = conv1(smooth_img[i], Dx, mode="reflect")
    for i in range(w):
        imgDy[:, i] = conv1(smooth_img[:, i], Dy, mode="reflect")
    return imgDx, imgDy