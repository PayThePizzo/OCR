#OCR 
This application convert images (.jpg) to editable documents (.docx extension)

It is divided in 
1. Image reading and Processing
2. Extraction of Characters

## 1A Acquiring the image - Image reading 
* Acquiring the file in the right format and convert it to the best usable one
* Resizing and Rescaling the file to make it readable

## 1B Preparing the image - Preprocessing
The possible modifications an image undergoes are the following: 

1. Inversion (Pixels from Black spectre become their opposite in the White one and viceversa)
2. Rescaling (Changing the width and height of an image)
3. Binarization 
4. Apply adaptive threshold to get a reasonably good binary mask.
5. Noise Removal (i.e. through Area Filter)
6. Improve cleaning segmentation with morphology
7. Dilation (+Thin lines) and Erosion (+Thick lines)
8. Rotation / Deskewing (Inverting the distorsion)
9. Add / Remove Borders
10. Transparency / Alpha Channel 
11. Blur / Sharpen


## Extraction of Character boundaries from Image
* Get the outer contours of each character and fit a bounding rectangle to each character blob.
* Crop each character using the previously calculated bounding rectangle.

## Building a Convolutional Neural Network(ConvNet) in remembering the Character images
Here we build a Character Recognition Model through CNN.


## Loading trained Convolutional Neural Network(ConvNet) Model


## Consolidating ConvNet predictions of characters


Source:
https://stackoverflow.com/questions/65738928/bounding-box-detection-for-characters-digits
https://medium.datadriveninvestor.com/4-simple-steps-in-building-ocr-1f41c66099c1
https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53
https://www.datacamp.com/community/tutorials/convolutional-neural-networks-python
https://www.digitalbangkokrecorder.com/blog/2017/02/programmatically-cleaning-document-scans/
https://www.analyticsvidhya.com/blog/2021/08/sharpening-an-image-using-opencv-library-in-python/
https://thenucleargeeks.com/2019/11/22/set-transparency-level-using-python-imaging-library-pillow/
https://note.nkmk.me/en/python-pillow-putalpha/
https://medium.com/analytics-vidhya/optical-character-recognition-using-tensorflow-533061285dd3