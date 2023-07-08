import numpy as np
import argparse
import os
import scipy.io as sio

parser = argparse.ArgumentParser(description='Algorithms traditional ML')
parser.add_argument('--dataset', type=str, required=True, \
            choices=["IP", "UP", "SV", "UH", "DIP", "DUP", "DIPr", "DUPr"], \
            help='dataset (options: IP, UP, SV, UH, DIP, DUP, DIPr, DUPr)')

data_path = os.path.join(os.getcwd(),'../HSI-datasets')
args = parser.parse_args()
if args.dataset  in ["IP", "DIP", "DIPr"]:
    data = sio.loadmat(os.path.join(data_path, 'indian_pines_corrected.mat'))['indian_pines_corrected']
    labels = sio.loadmat(os.path.join(data_path, 'indian_pines_gt.mat'))['indian_pines_gt']
    out_dir = os.path.join(data_path, 'IP_aug_np/')
elif args.dataset == 'SV':
    data = sio.loadmat(os.path.join(data_path, 'salinas_corrected.mat'))['salinas_corrected']
    labels = sio.loadmat(os.path.join(data_path, 'salinas_gt.mat'))['salinas_gt']
    out_dir = os.path.join(data_path, 'SV_aug/')
elif args.dataset  in ["UP", "DUP", "DUPr"]:
    data = sio.loadmat(os.path.join(data_path, 'paviaU.mat'))['paviaU']
    labels = sio.loadmat(os.path.join(data_path, 'paviaU_gt.mat'))['paviaU_gt']
    out_dir = os.path.join(data_path, 'UP_aug/')
elif args.dataset == 'UH':
    data = sio.loadmat(os.path.join(data_path, 'houston.mat'))['houston']
    labels = sio.loadmat(os.path.join(data_path, 'houston_gt.mat'))['houston_gt_tr']
    labels += sio.loadmat(os.path.join(data_path, 'houston_gt.mat'))['houston_gt_te']
    out_dir = os.path.join(data_path, 'UH_aug/')

print(data.shape)
print(labels.shape)

print(data.dtype)
print(labels.dtype)
def aug(n, data, labels):                                               #works for uint16 dtype as well
    for i in n:
        match i:
            case 1:                                                     # horizontalFlip(data, labels):
                flipped_image_data = np.fliplr(data)
                flipped_labels_data = np.fliplr(labels)

                return flipped_image_data, flipped_labels_data

            case 2:                                                       #verticalFlip(data, labels):
                flipped_image_data = np.flipud(data)
                flipped_labels_data = np.flipud(labels)

                return flipped_image_data, flipped_labels_data

            case 3:                                                       #horizontalRotation(data, labels):
                deg = np.random.choice([1,2,3])
                rotated_image_data = np.rot90(data, k=deg, axes=(1, 2))
                rotated_labels_data = np.rot90(labels, k=deg)

                return rotated_image_data, rotated_labels_data

            case 4:                                                        #verticalRotation(data, labels):
                deg = np.random.choice([1,2,3])
                rotated_image_data = np.rot90(data, k=deg, axes=(0, 1))
                rotated_labels_data = np.rot90(labels, k=deg)

                return rotated_image_data, rotated_labels_data

            case 5:                                                        #band_rearr(data):
                num_bands = data.shape[2]
                band_indices = np.random.permutation(num_bands)
                rearranged_image_data = data[:, :, band_indices]

                return rearranged_image_data, labels


n = [[1],[2],[3],[4],[5]]
for i in range(1, 6):
    for j in range(i + 1, 6):
        n.append([i, j])


# Apply augmentation and save the images
for i in range(len(n)):
    # Perform augmentation on the image

    augmented_image, augmented_labels = aug(n[i], data, labels)
    
    # Save the augmented image
    ImageName = f'augmented_image_{i}.mat'
    LabelName = f"augmented_labels_{i}.mat"
    ImagePath = os.path.join(out_dir, ImageName)
    LabelPath = os.path.join(out_dir, LabelName)

    image_data = {ImageName: augmented_image}
    sio.savemat(ImagePath, image_data)

    label_data = {LabelName: augmented_labels}
    sio.savemat(LabelPath, label_data)

