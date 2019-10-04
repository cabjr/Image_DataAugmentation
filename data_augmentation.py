import random
from scipy import ndarray
import skimage as sk
from skimage import transform
from skimage import util
import os, glob, cv2, argparse


parser = argparse.ArgumentParser()
parser.add_argument('--src', type=str, default=None, required=True, help='The source directory containing jpg images')
parser.add_argument('--dest', type=str, default="data/", required=True, help='The destination directory of transformed images')
args = parser.parse_args()

def random_rotation(image_array: ndarray):
    random_degree = random.uniform(-10, 10)
    return sk.transform.rotate(image_array, random_degree)

def random_noise(image_array: ndarray):
    return sk.util.random_noise(image_array)

def horizontal_flip(image_array: ndarray):
    return image_array[:, ::-1]

print(args.src)
print(args.dest)

list_imgs = [img for img in glob.glob(args.src+"/*.jpg")] 
"""+ [ img for img in glob.glob("./tipificacao/val/rgnback/*.jpg")]"""
#print(list_imgs)

available_transformations = {
    'rotate': random_rotation,
    'noise': random_noise,
    #'horizontal_flip': horizontal_flip
}


num_transformations_to_apply = random.randint(1, len(available_transformations))
num_files_desired = 1000
num_transformations = 0
transformed_image = None
for item in range(num_files_desired):
    key = random.choice(list(available_transformations))
    transformed_image = available_transformations[key](cv2.cvtColor(cv2.imread(random.choice(list_imgs)), cv2.COLOR_BGR2RGB))
    num_transformations += 1
    sk.io.imsave(args.dest+str(item)+".jpg", transformed_image)
