import os
import argparse
import PIL.Image as PILI

# Comply with os.makedirs - do not use parent dir. (..) in paths
ap = argparse.ArgumentParser()
ap.add_argument("in_dir")  # e.g. "inat18/"
ap.add_argument("out_dir")  # e.g. "out/"
ap.add_argument("--new_size", default=128)

args = ap.parse_args()

in_dir = args.in_dir
out_dir = args.out_dir
new_size = int(args.new_size)

for dirpath, dirnames, filenames in os.walk(in_dir):
    for img_name in filenames:
        # Skips empty directories
        img_path = dirpath + "/" + img_name
        resized_img = PILI.open(img_path)

        save_dir = out_dir + dirpath[len(in_dir):]
        
        os.makedirs(save_dir, exist_ok=True)
        
        # TODO: Should save in JPEG format
        
        print("Saved image:", save_dir + resized_img)
