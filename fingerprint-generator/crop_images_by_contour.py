import numpy as np
from skimage.morphology import convex_hull_image, binary_erosion
from PIL import Image
import glob
import os

def crop_fp(pil_img, binarization_threshold=220):

    img_mat = np.asarray(pil_img).copy()

    binarized_img_mat = np.where(img_mat > binarization_threshold, 0, 1)
    eroded_binary_img_mat = binary_erosion(binarized_img_mat)
    chull = convex_hull_image(eroded_binary_img_mat)

    indices = np.where(chull)
    y_min = indices[0].min()
    y_max = indices[0].max()
    x_min = indices[1].min()
    x_max = indices[1].max()

    return pil_img.crop((x_min, y_min, x_max, y_max))


IMG_PATH_PATTERN = '/home/dominik/RealScan/*.bmp'
OUT_DIR = '/home/dominik/RealScan'

os.makedirs(OUT_DIR, exist_ok=True)

mask_img_paths = glob.glob(IMG_PATH_PATTERN, recursive=True)

for input_path in mask_img_paths:

    img = Image.open(input_path)
    cropped_img = crop_fp(img)

    input_filename = os.path.split(input_path)[1]
    ext = os.path.splitext(input_filename)[1]
    output_filename = input_filename.replace(ext, '_cropped' + ext)
    output_path = os.path.join(OUT_DIR, output_filename)

    cropped_img.save(output_path)
