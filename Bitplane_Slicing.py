#----------------------------------------------------
#--- To perform Bit-Plane Slicing, i.e., decomposing 
#--- a digital image into a series of binary images, 
#--- each representing a specific bit position of 
#--- the pixel values.
#----------------------------------------------------
#--- Sangeeta Biswas, Ph.D.
#--- Associate Professor
#--- Department of Computer Science and Engineering
#--- University of Rajshahi
#--- Rajshahi-6205, Bangladesh
#----------------------------------------------------
# 02.08.2025
#----------------------------------------------------

#--- Import necessary modules
import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    #--- Load an image
    img_path = '/home/bibrity/CSE_Courses/CSE4161_DIP/Images/paddy_field1.jpeg'
    gray_img = cv2.imread(img_path, 0)

    #--- Slice an 8-bit image into 8 planes
    LSB_bits = []
    bit_planes = []
    for i in range(8):
    	#--- Step-1: Right-shift the pixel value by the bit plane number 
    	#--- to move the target bit to the LSB position.
    	bit_shifted_img = gray_img >> i

    	#--- Step-2: Perform a bitwise AND operation with 1 to extract
    	#--- the value of that LSB (either 0 or 1).
    	LSB_bit = bit_shifted_img & 1
    	LSB_bits.append(LSB_bit)

    	#--- Step-3: Multiply the extracted  LSB bit by 255 to create
    	#--- a binary image
    	sliced_img = LSB_bit * 255

    	bit_planes.append(sliced_img)

    #--- Combined different bit-planes to reconstruct the grayscale image
    cmd_img1 = (bit_planes[0] + bit_planes[1] + bit_planes[2]) * 255
    cmd_img2 = (bit_planes[3] + bit_planes[4] + bit_planes[5]) * 255
    cmd_img3 = (bit_planes[5] + bit_planes[6] + bit_planes[7]) * 255

    #--- Display images
    img_set = [gray_img]
    img_set += bit_planes
    img_set += [cmd_img1, cmd_img2, cmd_img3]

    title_set = ['Gray', 'Bit_Plane-1', 'Bit_Plane-2', 'Bit_Plane-3', 
    			'Bit_Plane-4', 'Bit_Plane-5', 'Bit_Plane-6', 'Bit_Plane-7',
    			'Bit_Plane-8', 'Plane_1+2+3', 'Plane_4+5+6', 'Plane_6+7+8']
    color_set = ['gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 
    			'gray', 'gray', 'gray', 'gray', 'gray']
    display_imgset(img_set, color_set, title_set, row = 4, col = 3)

def display_imgset(img_set, color_set, title_set = '', row = 1, col = 1):
	plt.figure(figsize = (20, 20))
	k = 1
	for i in range(1, row + 1):
		for j in range(1, col + 1):
			plt.subplot(row, col, k)
			plt.axis('off')
			img = img_set[k-1]
			if(len(img.shape) == 3):
				plt.imshow(img)
			else:
				plt.imshow(img, cmap = color_set[k-1])
			if(title_set[k-1] != ''):
				plt.title(title_set[k-1])
			k += 1
		
	plt.show()
	plt.close()

if __name__ == '__main__':
	main()
