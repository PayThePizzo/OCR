import cv2 as cv
from matplotlib import pyplot as plt


def open_image(path):
    """
    Opens an image from path

    :param path: The absolute filepath of the image (i.e. r'C:\Users\...\img.png')
    :return: An image file
    """
    img = cv.imread(path)
    # cv.imshow('Original Image', img)
    # cv.waitKey(0)
    return img


def display(im_path):
    dpi = 80
    im_data = plt.imread(im_path)

    height, width = im_data.shape[:2]

    # What size does the figure need to be in inches to fit the image?
    figsize = width / float(dpi), height / float(dpi)

    # Create a figure of the right size with one axes that takes up the full figure
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])

    # Hide spines, ticks, etc.
    ax.axis('off')

    # Display the image.
    ax.imshow(im_data, cmap='gray')

    plt.show()


def invert():
    """
    Inverts the pixels of an image

    :return:
    Inverted image file
    """

    pass


def binarize():
    pass


def noise_reduction():
    pass


def dilatate():
    pass


def erode():
    pass


def rotate():
    pass


def deskew():
    pass


def remove_borders():
    pass


def add_borders():
    pass


def padding():
    pass
