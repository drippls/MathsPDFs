#!/bin/bash
cd ../
source venv/bin/activate
cd imgs

magick mogrify -monitor -format jpg *.HEIC
find . -depth 1 -name "*.HEIC" -delete

cd ../src
python3 main.py assignment

deactivate

# folder = date +%m-%d-%Y
# cd ../imgs
# mkdir $folder
# mv * $folder
# mv $folder ../old_images
