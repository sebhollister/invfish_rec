from PIL import Image
import glob
import os

def convert_to_jpg(folder_name):
    fish_name = folder_name.split("/")[2]
    for i, filepath in enumerate(glob.iglob(folder_name)):    
        im = Image.open(filepath)
        rgb_im = im.convert('RGB')
        rgb_im.save('data/fish/{}/{}{}.jpg'.format(fish_name, fish_name, i))

if __name__ == "__main__":
    #folder_name = 'data/fish/blue_tang/*'
    folder_name = 'data/fish/clownfish/*'
    convert_to_jpg(folder_name)