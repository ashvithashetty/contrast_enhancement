import matplotlib.pyplot as plt 
from PIL import Image
import numpy as np

def std_dev_stretch(image,k):
	img=plt.imread(image)
	out = np.zeros_like(img)

	#extract individual bands
	red,green,blue=img[:,:,0],img[:,:,1],img[:,:,2]

	red=red.astype(float)
	red_mean=red.mean()
	red_std=red.std()
	red_min=red_mean-(k*red_std)
	red_max=red_mean+(k*red_std)
	red_range=(red_max-red_min)
	red_new= ((red - red_min)* 255/red_range)
	red_new[red_new<0]=0
	red_new[red_new>255]=255


	green=green.astype(float)
	green_mean=green.mean()
	green_std=green.std()
	green_min=green_mean-(k*green_std)
	green_max=green_mean+(k*green_std)
	green_range=(green_max-green_min)
	green_new=((green - green_min)*255/green_range)
	green_new[green_new<0]=0
	green_new[green_new>255]=255


	blue=blue.astype(float)
	blue_mean=blue.mean()
	blue_std=blue.std()
	blue_min=blue_mean-(k*blue_std)
	blue_max=blue_mean+(k*blue_std)
	blue_range=(blue_max-blue_min)
	blue_new= ((blue - blue_min)*255/blue_range)
	blue_new[blue_new<0]=0
	blue_new[blue_new>255]=255


	out[:,:,0]=red_new
	out[:,:,1]=green_new
	out[:,:,2]=blue_new

	plt.subplot(1,2,1)
	plt.imshow(img)
	plt.axis("off")
	plt.title("Input Image")
	plt.subplot(1,2,2)
	plt.imshow(out.astype(np.uint8))
	plt.axis("off")
	plt.title('Output Image')
	plt.show()
	plt.imsave('output.jpg',out)

# std_dev_stretch('Sample_Input/example1.jpg',1.6)