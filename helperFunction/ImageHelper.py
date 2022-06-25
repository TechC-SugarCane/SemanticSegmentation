import pathlib
import shutil
from PIL import Image
import os


def change_file_extention(file, to_suffix):
    st = pathlib.PurePath(file).stem
    to_file = st + to_suffix

    from_file_path = os.path.join("./dataset/", file)
    to_file_path = os.path.join("./dataset/", to_file)

    shutil.move(from_file_path, to_file_path)


def resize_image(img_path, IMAGE_SIZE=256):
    for image in img_path:
        img = Image.open(image)

        img_resize = img.resize((IMAGE_SIZE, IMAGE_SIZE))
        img_resize.save(f'{image}', quality=90)


# 画像量産
def increase_image(image, degree=5, step=5):
    img_name = pathlib.PurePath(image).stem
    img = Image.open(image)

    for x in range(degree, 360, step):
        img = img.copy()
        rotate_img = img.rotate(x)
        rotate_img.save(f'./dataset/{img_name}_{x}.png')


