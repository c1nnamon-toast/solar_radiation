import os
import glob

from PIL import Image
import numpy as np
from tqdm import tqdm

def count_black_pixels_from_side(img_array, side):
    if side == 'top':
        for i in range(0, img_array.shape[0], 1):
            if not np.all(img_array[i, :] == 0):
                return i

        return img_array.shape[0]
    
    if side == 'bottom':
        for i in range(img_array.shape[0] - 1, -1, -1):
            if not np.all(img_array[i, :] == 0):
                return img_array.shape[0] - 1 - i

        return img_array.shape[0]
    
    if side == 'left':
        for i in range(0, img_array.shape[1], 1):
            if not np.all(img_array[:, i] == 0):
                return i

        return img_array.shape[1]
    
    if side == 'right':
        for i in range(img_array.shape[1] - 1, -1, -1):
            if not np.all(img_array[:, i] == 0):
                return img_array.shape[1] - 1 - i

        return img_array.shape[1]
    
    return 0


def calculate_border(dataset_path):
    png_files = glob.glob(os.path.join(dataset_path, "**", "*.png"), recursive=True)
    
    print(f"Dataset size: {len(png_files)}")
    
    min_top = float('inf')
    min_bottom = float('inf')
    min_left = float('inf')
    min_right = float('inf')
    
    for img_path in tqdm(png_files, desc="Calculating border"):
        img = Image.open(img_path)
        img_array = np.array(img)
        
        top = count_black_pixels_from_side(img_array, 'top')
        bottom = count_black_pixels_from_side(img_array, 'bottom')
        left = count_black_pixels_from_side(img_array, 'left')
        right = count_black_pixels_from_side(img_array, 'right')
        
        min_top = min(min_top, top)
        min_bottom = min(min_bottom, bottom)
        min_left = min(min_left, left)
        min_right = min(min_right, right)
    
    print(f"Minimal Border\nTop: {min_top}\nBottom: {min_bottom}\nLeft: {min_left}\nRight: {min_right}")
    
    return min_top, min_bottom, min_left, min_right


def crop_images(dataset_path, top=32, bottom=100, right=66, left=66):
    output_base = os.path.join(
        os.path.dirname(dataset_path), 
        os.path.basename(dataset_path) + '_cropped')
    
    png_files = glob.glob(os.path.join(dataset_path, "**", "*.png"), recursive=True)
    
    print(f"\nFound {len(png_files)} images")
    
    original_dims = None
    new_dims = None
    
    for img_path in tqdm(png_files, desc="Cropping images", delay=1):
        img = Image.open(img_path)
        
        if original_dims is None:
            original_dims = img.size
            print(f"Original dimensions: {original_dims[0]}x{original_dims[1]}")
        
        width, height = img.size
        crop_box = (left, top, width - right, height - bottom)
        
        cropped_img = img.crop(crop_box)
        
        if new_dims is None:
            new_dims = cropped_img.size
            print(f"New dimensions: {new_dims[0]}x{new_dims[1]}")
        
        relative_path = os.path.relpath(img_path, dataset_path)
        output_path = os.path.join(output_base, relative_path)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        cropped_img.save(output_path)

    print(f"Cropping complete. Images saved to {output_base}")


if __name__ == "__main__":
    dataset_path = "./expo10_Alpnach2018"
    
    top, bottom, left, right = calculate_border(dataset_path)
    crop_images(dataset_path, top, bottom, left, right)
