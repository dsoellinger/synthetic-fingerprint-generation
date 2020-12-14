import os
import glob

def get_fingerprint_images_list(base_path, HR_true, img_ext='.bmp'):

    if HR_true:
        search_pattern = os.path.join(base_path, '**/*_cropped_resized_HR' + img_ext)
    else:
        search_pattern = os.path.join(base_path, '**/*_cropped_resized_LR' + img_ext)

    img_paths = glob.glob(search_pattern, recursive=True)

    return img_paths
