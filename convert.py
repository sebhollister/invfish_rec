from PIL import Image
import glob
import os

for i, filepath in enumerate(glob.iglob(r'data/fish/blue_tang/*')):    
    im = Image.open(filepath)
    rgb_im = im.convert('RGB')
    rgb_im.save('data/fish/blue_tang/blue_tang{}.jpg'.format(i))



# im = Image.open("Ba_b_do8mag_c6_big.png")
# rgb_im = im.convert('RGB')
# rgb_im.save('colors.jpg')