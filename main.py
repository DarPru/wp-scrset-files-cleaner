import os
import re
from PIL import Image

dir = 'test'


def trash_img_remover(location: dir):
    try:
        for path, directories, files in os.walk(dir):
            for file in files:
                if re.search('-\d{2,4}x\d{2,4}.', file):
                    print(f'deleting {file}...')
                    os.remove(os.path.join(path, file))
    except Exception as e:
        print(f'Error: {e}')

    finally:
        print('Task is complete!')


def minify_imgs(location=dir):
    try:
        for path, directories, files in os.walk(dir):
            for file in files:
                picture = Image.open(os.path.join(path, file))
                rgb_picture = picture.convert('RGB')
                rgb_picture.save(os.path.join(path, file), optimize=True, quality=10)
                print(f'{file} is minified')
    except Exception as Ex:
        print(f'Error minifying file: {Ex}')
    finally:
        print('Minification is over!')


if __name__ == '__main__':
    # trash_img_remover(location=dir)
    minify_imgs(location=dir)
