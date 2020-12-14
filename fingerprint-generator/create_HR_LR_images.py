from PIL import Image
from torchvision.transforms.functional import five_crop as torch_five_crop, resize as torch_resize

from fingerprints_dataset import get_fingerprint_images_list


def save_resized_image(path, HR_image_size, LR_image_size):
    img = Image.open(path)
    resized = torch_resize(img, HR_image_size)
    HR = torch_five_crop(resized, HR_image_size)[-1]
    HR.save(path[:-4] + "_resized_HR.bmp", "BMP")
    LR = torch_resize(HR, LR_image_size)
    LR.save(path[:-4] + "_resized_LR.bmp", "BMP")


images = get_fingerprint_images_list('/scratch2/dsoellinger/RealScan/', load_cropped=True, img_ext='.bmp')
for idx, image in enumerate(images):
    if not image.endswith('_cropped.bmp'):
        print(image)
        continue
    save_resized_image(image, 256, 64)
    if idx % 1000 == 0:
        print("{}/{} processed".format(idx + 1, len(images)))
