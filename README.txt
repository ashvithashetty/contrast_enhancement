# contrast_enhancement
### Contrast Enhancement using Standard Deviation Stretch

Given a low contrast RGB image, the range of gray levels in each band is stretched to occupy the entire dynamic range of gray levels of the display device. The extent of enhancement depends on parameter 'k'.
Assumption:Maximum gray level of the display device is 255. 

Function `std_dev_stretch` takes two arguments,
- image : low contrast input image
- k : often a value between 1 and 2

Output image is saved in  a file 'output.jpg'.

![screenshot2](https://user-images.githubusercontent.com/8946566/27991229-95b747cc-648d-11e7-9813-e9feb990c011.jpg)
