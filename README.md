Dataset link (HSI-dataset) : [https://drive.google.com/file/d/1nq50BuDh7LaAg62g_nTlKRIy2NZpxfYc/view?usp=sharing](url)

To take an Hyperspectral image and augment it to create an expanded dataset. 

Processing methods performed :
1) horizontal flip
2) vertical flip
3) horizontal rotation
4) vertical rotation
5) band shuffling

using numpy to augment the images, made it suitable for all dtypes.

View.py - used to view either a specific band or all the bands of the image.

# SV HSI (band 100) original
![Band_SV_3_200](https://github.com/anusha-adhikari/HSI_aug/assets/74814765/1c109bd0-573d-4fcf-9f5d-011ac8df4b56)

# SV HSI (band 100) after augmentation
