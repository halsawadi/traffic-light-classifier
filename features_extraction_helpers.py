# Features-extraction Helpers

import matplotlib.pyplot as plt
import cv2
import numpy as np

# This function cuts down thee given image to the new height and width supplied as arguments
def centre_crop_image(im, height, width):
    # Args:
        # im: the original image.
        # height: the new height.
        # width: the new width.
    # Returns: the resultant cropped image 
    
    if (height <= 32 and height > 0 and width <= 32 and width > 0):
        
        original_height = im.shape[0]
        original_width = im.shape[1]
        v_margin = int((original_height-height)/2)
        h_margin = int((original_width-width)/2)
        
        return im[v_margin:(original_height - v_margin), h_margin:(original_width - h_margin)]
    return ValueError("Either the wanted width or height is higher than the actual width or height, respectively.")


# This function calculates the mean brightness for the given image.
def compute_average_brightness(rgb_im, axis):
    #args:
        # rgb_im: the input image described in RGB colour space
        # axis: the axis in which the average brightness is computes
    hsv_im = cv2.cvtColor(rgb_im, cv2.COLOR_RGB2HSV)
    return np.mean(hsv_im[:,:,2], axis = axis)



# This function plot the three channels for the given image of any color space beside to the original image.
def run_components_visualization(im, color_space):
    # Args:
        # im: the original image
        # color_space: a string which specifies the color space of the given image im.
        
    C1 = im[:,:,0]
    C2 = im[:,:,1]
    C3 = im[:,:,2]
    
    t1 = color_space[0]
    t2 = color_space[1]
    t3 = color_space[2]
    
    f, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(20,10))
    ax1.set_title('Original image')
    ax1.imshow(im)
    ax2.set_title(t1 + ' channel')
    ax2.imshow(C1, cmap='gray')
    ax3.set_title(t2 + ' channel')
    ax3.imshow(C2, cmap='gray')
    ax4.set_title(t3 + ' channel')
    ax4.imshow(C3, cmap='gray')
