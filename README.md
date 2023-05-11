# Walaris Track Anything Test Repo

This repo provides an easy testing environment for the track anything algorithm. This algorithm combines SAM (https://arxiv.org/abs/2304.02643) and XMEM (https://arxiv.org/pdf/2207.07115.pdf) to perform object tracking on videos.

# How To Use

Follow the official tutorial found here: https://github.com/gaomingqi/Track-Anything/blob/master/doc/tutorials.md.

This custom application works much in the same way as the original application, but it has been modified to fit our use case of creating bounding box labels for videos.

Load your images and manually add the initial mask following the original tutorial as a reference. Once you have tracked the object, your video, images, and labels.txt file will appear in the `Track-Anything/labels` directory.

# Initial Testing Results

## Visible Light
![alt text](https://github.com/GraysonWalaris/track_anything_testing/blob/main/test_results/multi_mask_tracking.gif)

## Thermal
UAV

![alt text](https://github.com/GraysonWalaris/track_anything_testing/blob/main/test_results/thermal_uav_tracking.gif)
Bird

Left (Untracked)                 Right (Tracked)

![alt text](https://github.com/GraysonWalaris/track_anything_testing/blob/main/test_results/thermal_bird_11.gif)
![alt text](https://github.com/GraysonWalaris/track_anything_testing/blob/main/test_results/thermal_bird_11_tracking.gif)

