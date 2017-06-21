# contrast_enhancement
Contrast Enhancement using Standard Deviation Stretch

Given a low contrast RGB image, the range of gray levels in each band is stretched to occupy the entire dynamic range of 
gray levels of the display device. The extent of enhancement depends on parameter 'k'.
Assumption:Maximum gray level of the display device is 255. 

Function std_dev_stretch takes two arguments;
	image : low contrast input image
	k : often a value between 1 and 2
	output image is saved in  a file 'output.jpg'