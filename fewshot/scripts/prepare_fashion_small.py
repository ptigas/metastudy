import json
import os
import shutil
import sys

import numpy as np
from tqdm import tqdm as tqdm

from config import DATA_PATH
from few_shot.utils import mkdir
from few_shot.utils import rmdir

path_to_fashion = sys.argv[1]

background_classes = list(
    map(
        lambda x: x.strip(), "\
Cufflinks, Rompers, Laptop Bag, Sports Sandals, Hair Colour,\
Suspenders, Trousers, Kajal and Eyeliner, Compact, Concealer, Jackets, Mufflers,\
Backpacks, Sandals, Shorts, Waistcoat, Watches, Pendant, Basketballs, Bath Robe,\
Boxers, Deodorant, Rain Jacket, Necklace and Chains, Ring, Formal Shoes, Nail Polish,\
Baby Dolls, Lip Liner, Bangle, Tshirts, Flats, Stockings, Skirts, Mobile Pouch, Capris,\
Dupatta, Lip Gloss, Patiala, Handbags, Leggings, Ties, Flip Flops, Rucksacks, Jeggings,\
Nightdress, Waist Pouch, Tops, Dresses, Water Bottle, Camisoles, Heels, Gloves, Duffel\
Bag, Swimwear, Booties, Kurtis, Belts, Accessory Gift Set, Bra\
".split(',')))

evaluation_classes = list(
    map(
        lambda x: x.strip(), "\
Jeans, Bracelet, Eyeshadow, Sweaters, Sarees, Earrings, Casual Shoes,\
Tracksuits, Clutches, Socks, Innerwear Vests, Night suits, Salwar, Stoles, Face\
Moisturisers, Perfume and Body Mist, Lounge Shorts, Scarves, Briefs, Jumpsuit, Wallets,\
Foundation and Primer, Sports Shoes, Highlighter and Blush, Sunscreen, Shoe\
Accessories, Track Pants, Fragrance Gift Set, Shirts, Sweatshirts, Mask and Peel,\
Jewellery Set, Face Wash and Cleanser, Messenger Bag, Free Gifts, Kurtas, Mascara,\
Lounge Pants, Caps, Lip Care, Trunk, Tunics, Kurta Sets, Sunglasses, Lipstick, Churidar,\
Travel Accessory\
".split(',')))

# Clean up folders
rmdir(DATA_PATH + '/fashion_small/images_background')
rmdir(DATA_PATH + '/fashion_small/images_evaluation')

# Create class folders
for c in background_classes:
  mkdir(DATA_PATH + f'/fashion_small/images_background/{c}/')

for c in evaluation_classes:
  mkdir(DATA_PATH + f'/fashion_small/images_evaluation/{c}/')

root = path_to_fashion + '/images'
with open(path_to_fashion + '/styles.csv') as f:
  for line in tqdm(f.readlines()[1:]):
    line = line.split(',')
    class_name = line[4]
    if class_name in evaluation_classes:

      subset_folder = 'images_evaluation'
    elif class_name in background_classes:
      subset_folder = 'images_background'
    else:
      # skip
      continue

    _id = int(line[0])
    image_name = line[0]
    #print(_id, subset_folder)
    try:
      src = f'{root}/{_id}.jpg'
      dst = DATA_PATH + f'/fashion_small/{subset_folder}/{class_name}/{image_name}'
      shutil.copy(src, dst)
    except Exception as e:
      print(e)
