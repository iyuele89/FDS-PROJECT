import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

import histogram_module
import dist_module

def rgb2gray(rgb):

    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray


# model_images - list of file names of model images
# query_images - list of file names of query images
#
# dist_type - string which specifies distance type:  'chi2', 'l2', 'intersect'
# hist_type - string which specifies histogram type:  'grayvalue', 'dxdy', 'rgb', 'rg'
#
# note: use functions 'get_dist_by_name', 'get_hist_by_name' and 'is_grayvalue_hist' to obtain 
#       handles to distance and histogram functions, and to find out whether histogram function 
#       expects grayvalue or color image


def find_best_match(model_images, query_images, dist_type, hist_type, num_bins):

    hist_isgray = histogram_module.is_grayvalue_hist(hist_type)
    
    model_hists = compute_histograms(model_images, hist_type, hist_isgray, num_bins)
    query_hists = compute_histograms(query_images, hist_type, hist_isgray, num_bins)
    
    D = np.zeros((len(query_hists), len(model_hists)))

    for i in range(len(query_hists)):
        for j in range(len(model_hists)):
            D[i, j] = dist_module.get_dist_by_name(query_hists[i], model_hists[j], dist_type)

    best_match = np.argmin(D, axis=1)
    return best_match, D


def compute_histograms(image_list, hist_type, hist_isgray, num_bins):
    
    image_hist = []

    for i in range(len(image_list)):
        img = np.array(Image.open(image_list[i])).astype('double')
        tmp = histogram_module.get_hist_by_name(img, num_bins, hist_type)

        # Compute hisgoram for each image and add it at the bottom of image_hist
        image_hist.append(tmp)

    return image_hist


# For each image file from 'query_images' find and visualize the 5 nearest images from 'model_image'.
#
# Note: use the previously implemented function 'find_best_match'
# Note: use subplot command to show all the images in the same Python figure, one row per query image

def show_neighbors(model_images, query_images, dist_type, hist_type, num_bins):

    best, D = find_best_match(model_images, query_images, dist_type, hist_type, num_bins)
    plt.figure(figsize=(30, 10))

    num_nearest = 5  # show the top-5 neighbors

    for i in range(len(query_images)):
        ind = np.argsort(D[i, :])  # indices of the 5 neighbors
        # Plot the queryimages
        plt.subplot(len(query_images), num_nearest + 1, i * (num_nearest + 1) + 1)
        img = np.array(Image.open(query_images[i]))
        plt.imshow(img)

        # Plot the 5 neighbors
        for j in range(num_nearest):
            plt.subplot(len(query_images), num_nearest + 1, i * (num_nearest + 1) + j + 1 + 1)
            img = np.array(Image.open(model_images[ind[j]]))
            plt.imshow(img)

    plt.show()

