import os
import scipy.io as sio
import numpy as np
import argparse
import matplotlib.pyplot as plt
'''
parser = argparse.ArgumentParser(description='Algorithms traditional ML')
parser.add_argument('--dataset', type=str, required=True, \
            choices=["IP", "UP", "SV", "UH", "DIP", "DUP", "DIPr", "DUPr"], \
            help='dataset (options: IP, UP, SV, UH, DIP, DUP, DIPr, DUPr)')

data_path = os.path.join(os.getcwd(),'../HSI-datasets')
#data = sio.loadmat(os.path.join(data_path, 'indian_pines_corrected.mat'))['indian_pines_corrected']
#labels = sio.loadmat(os.path.join(data_path, 'indian_pines_gt.mat'))['indian_pines_gt']
#data = sio.loadmat(os.path.join(data_path, 'salinas_corrected.mat'))['salinas_corrected']
args = parser.parse_args()
if args.dataset  in ["IP", "DIP", "DIPr"]:
  data = sio.loadmat(os.path.join(data_path, 'indian_pines_corrected.mat'))['indian_pines_corrected']
  out_dir = os.path.join(data_path, 'HSI_bandimg/IP/')
elif args.dataset == 'SV':
  data = sio.loadmat(os.path.join(data_path, 'salinas_corrected.mat'))['salinas_corrected']
  out_dir = os.path.join(data_path, 'HSI_bandimg/SV/')
elif args.dataset  in ["UP", "DUP", "DUPr"]:
  data = sio.loadmat(os.path.join(data_path, 'paviaU.mat'))['paviaU']
  out_dir = os.path.join(data_path, 'HSI_bandimg/UP/')
elif args.dataset == 'UH':
  data = sio.loadmat(os.path.join(data_path, 'houston.mat'))['houston']
  out_dir = os.path.join(data_path, 'HSI_bandimg/UH/')
'''
data_path = os.path.join(os.getcwd(),'../HSI-datasets')
data = sio.loadmat(os.path.join(data_path, 'SV_aug/augmented_image_11.mat'))['augmented_image_11.mat']
'''
mat_data = sio.loadmat(os.path.join(data_path, 'SV_aug/augmented_image_3.mat'))

# Get the keys from the loaded data
keys = mat_data.keys()

# Print the keys
for key in keys:
    print(key)
'''
print(data.shape)

num_bands = data.shape[2]
#print(labels.shape)

#print(np.array(labels)[:5])
#print(np.array(data)[0, :5])

# Assuming you have a hyperspectral image with shape (height, width, 200) stored in the variable "hyperspectral_image"
# Convert the image to RGB by assigning different bands to the red, green, and blue channels
#red_band = data[:, :, 50]  # Assigning the 50th band to the red channel
#green_band = data[:, :, 100]  # Assigning the 100th band to the green channel
#blue_band = data[:, :, 150]  # Assigning the 150th band to the blue channel

# Stack the bands together to create an RGB image
#rgb_image = np.stack([red_band, green_band, blue_band], axis=-1)
#omin = np.min(rgb_image)
#omax = np.max(rgb_image)

#print(rgb_image.dtype)

#normalized_image = (rgb_image - omin) / (omax - omin)
#print(normalized_image.shape)
#print(normalized_image.dtype)
#normalized_image = normalized_image.astype(np.float32)

#print(np.min(normalized_image))
#print(np.max(normalized_image))

# Display the RGB image
#plt.imshow(normalized_image)
#plt.show()

#data1 = data[:, :, 1]
#print(data1.shape)


'''
for i in range(num_bands):
  img_band = data[:, :, i]
  #plt.title(f"Band = {i}")
  filename = f'Band_{i}.jpg'
  filepath = os.path.join(out_dir, filename)
  plt.imshow(img_band, cmap = "nipy_spectral")
  plt.axis('off')
  plt.savefig(filepath, format='jpg', dpi=300)
'''

out_dir = os.path.join(data_path, 'HSI_bandimg/SV/')

img_band = data[:, :, 200]
#plt.title(f"Band = {i}")
filename = f'Band_SV_11_200.jpg'
filepath = os.path.join(out_dir, filename)
plt.imshow(img_band, cmap = "nipy_spectral")
plt.axis('off')
plt.savefig(filepath, format='jpg', dpi=300)
